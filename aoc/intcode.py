"""
IntCode Computer WIP

Currently implemented up to day 5 pt 2

Ideas for future improvments
 - Add a deque based StdIO implementation,
   useful for preseeding input, catching output
 - Split out intcode to a module with subfiles, it's getting a bit large
    - Computer
    - Instructions?
        - OpCode stuff
        - Maybe create a parent instruction class handling Arguments, OpCodes
          and execution of instruction thus seperating it from core computer.
          This could also ease potential future expansion such as intrerupt
          handling, multi tenancy system, non real time os, etc
    - IO
    - Addresses/Arguments
        - ParamMode
    - Errors
 - Move some stuff into Computer class?
 - Add more logging
 - ...

"""
from dataclasses import dataclass, field
from enum import IntEnum
from functools import partial
from itertools import permutations, zip_longest
from numbers import Number
from typing import Tuple, Iterable, List, NoReturn, Dict
import logging

from more_itertools import ilen


# Custom exceptions for error handling in intcode computer
class ExecutionError(Exception):
    pass


class ExecutionFinished(Exception):
    pass


# Classes used in IntCode Computer

# Default STDIN/STDOUT implementation
class StdIO:
    def write(self, data: int) -> NoReturn:
        print("STDOUT:")
        print(data)

    def read(self) -> int:
        return int(input())


DEFAULT_IO = StdIO()


# OpCodes
class OpCode(IntEnum):
    ADD = 1
    MUL = 2

    # Day 5 pt1
    MOVS = 3
    OUT = 4
    # Day 5 pt2
    JMPT = 5
    JMPF = 6
    LT = 7
    EQ = 8

    HALT = 99


class ParamMode(IntEnum):
    "The parameter mode to use"

    POSITION = 0
    "Pass by reference"

    IMMEDIATE = 1
    "Pass by value"


@dataclass
class Arg:
    val: int
    pos: int
    memory: List
    mode: ParamMode = ParamMode.POSITION

    @property
    def value(self) -> int:
        if self.mode == ParamMode.POSITION:
            return self.memory[self.val]
        elif self.mode == ParamMode.IMMEDIATE:
            return self.val

    def store(self, new_value: int):
        if self.mode == ParamMode.POSITION:
            self.memory[self.val] = new_value
        elif mode == ParamMode.IMMEDIATE:
            self.memory[self.pos] = new_value

    def __int__(self) -> int:
        return self.value


# Types
Instruction = Tuple[OpCode, int, int, int]


@dataclass
class Address:
    # These are currently only used for return addresses, could possible be
    # useful for all addresses in the future
    value: int
    relative: bool = True

    def next_addr(self, pos):
        if self.relative:
            return pos + self.value
        # Absolute addressing, unsued for now but useful if we add statments
        # Like GOTO, JMP, etc.
        return self.value


# Operation implementations
def add(a: Arg, b: Arg, c: Arg, memory: List) -> Address:
    """
    Three arguments 1, 2, 3
    Adds the values of pos at val(1), val(2)
    Store in pos val(3)
    Return: Next instruction address
    """
    c.store(int(a) + int(b))
    return Address(4)


def mul(a: Arg, b: Arg, c: Arg, memory: List) -> Address:
    """
    Three arguments 1, 2, 3
    Adds the multiplies of pos at val(1), val(2)
    Store in pos at val(3)
    Return: Next instruction address
    """
    c.store(int(a) * int(b))
    return Address(4)


def halt(*_, **kwargs):
    """ Program is done, finish """
    raise ExecutionFinished("Reached halt")


def movs(addr: Arg, memory: List, io: StdIO = DEFAULT_IO) -> Address:
    """ Read from stdin, write to given address """
    addr.store(int(io.read()))
    return Address(2)


def out(addr: Arg, memory: List, io: StdIO = DEFAULT_IO) -> Address:
    """Write from addr to stdout"""
    io.write(int(addr))
    return Address(2)


def jump_if_true(cond: Arg, addr: Arg, memory: List) -> Address:
    """
    jump-if-true: if the first parameter is non-zero, it sets the instruction
    pointer to the value from the second parameter. Otherwise, it does nothing.
    """
    if int(cond) != 0:
        return Address(int(addr), relative=False)
    return Address(3)


def jump_if_false(cond: Arg, addr: Arg, memory: List) -> Address:
    """
    jump-if-false: if the first parameter is zero, it sets the instruction
    pointer to the value from the second parameter. Otherwise, it does nothing.
    """
    if int(cond) == 0:
        return Address(int(addr), relative=False)
    return Address(3)


def less_than(a: Arg, b: Arg, addr: Arg, memory: List) -> Address:
    """
    less than: if the first parameter is less than the second parameter, it
    stores 1 in the position given by the third parameter.
    Otherwise, it stores 0.
    """
    addr.store(int(int(a) < int(b)))
    return Address(4)


def equals(a: Arg, b: Arg, addr: Arg, memory: List) -> Address:
    """
    equals: if the first parameter is equal to the second parameter, it stores
    1 in the position given by the third parameter. Otherwise, it stores 0.
    """
    addr.store(int(int(a) == int(b)))
    return Address(4)


# OpCode to implementation mapper
function_map = {
    OpCode.ADD: add,
    OpCode.MUL: mul,
    OpCode.MOVS: movs,
    OpCode.OUT: out,
    OpCode.HALT: halt,
    OpCode.JMPT: jump_if_true,
    OpCode.JMPF: jump_if_false,
    OpCode.LT: less_than,
    OpCode.EQ: equals,
}


@dataclass
class Computer:
    "Naïve computer implementation"

    memory: List[int]
    "Memory shouldn't be a arbitrary iterator as we will access it by index"

    io: StdIO = DEFAULT_IO

    pos: int = field(default=0, init=False)
    "Position of current op code"

    def __post_init__(self):
        if not isinstance(self.memory, List):
            # PyDantic can do this automatically
            raise ExecutionError(
                "Incompatible memory, needs to be RAM(List) not ROM(Tuple)"
            )

    def __parse_op_code(self, code: int) -> Tuple[OpCode, Iterable[Arg]]:
        code = str(code)
        op = OpCode(int(code[-2:]))
        args = self.get_args(op, (ParamMode(int(arg)) for arg in reversed(code[:-2])))
        return op, args

    def __num_args(op: OpCode) -> int:
        """
        Returns number of the function arguments are IntCode `Arg` parameters
        """
        return ilen(
            1 for (arg, t) in function_map[op].__annotations__.items() if t == Arg
        )

    def get_args(self, op: OpCode, param_modes: Iterable[ParamMode]) -> Iterable[Arg]:
        """Returns arguments `Arg` for given instruction"""
        # Uses functions airty as step size and as slice size
        arg_values = self.memory[self.pos + 1 : self.pos + 1 + Computer.__num_args(op)]
        return (
            Arg(arg_val, arg_pos, self.memory, pmode)
            for (pmode, (arg_pos, arg_val)) in zip_longest(
                param_modes,
                enumerate(arg_values, start=self.pos + 1),
                fillvalue=ParamMode.POSITION,
            )
        )

    def __instruction(self) -> Instruction:
        try:
            yield self.__parse_op_code(self.memory[self.pos])
        except IndexError:
            # Better error incase someone loads invalid programs
            raise ExecutionError("Invalid program, memory out of bounds")
        except ValueError as e:
            # Invalid OpCode, raise error
            raise e

    def __execute(self, instruction: Instruction) -> NoReturn:
        """
        Execute instruction, mutating memory.

        Raises ProgramFinished when halt is reached.

        Args:
            instruction: The instruction (with arguments) to execute
        """

        op, args = instruction
        logging.debug(f"Executing: {op}")
        logging.debug(self.memory)

        # Prepare functions by injecting external hardware
        # Keyboard and monitor for now
        # This breaks argument introspections so it's applied after that step.
        func = function_map[op]
        if key := next(
            (
                param
                for param, type_ in func.__annotations__.items()
                if type_ == StdIO
            ),
            False,
        ):
            func = partial(func, **{key: self.io})

        self.pos = func(*list(args), memory=self.memory).next_addr(
            self.pos
        )
        logging.debug(self.memory)

    def run_program(self) -> bool:
        """
        Returns true if execution stops at a halt
        """
        try:
            while instruct := next(self.__instruction()):
                self.__execute(instruct)
        except ExecutionFinished:
            # Program finished
            return True
        # Program finished without halt
        return False

    def read(self, memory_index: int = 0):
        """Returns memory at given postion (or first)"""
        return self.memory[memory_index]


def restore_program(memory_updates: Dict[int, int], memory: List[int]) -> List[int]:
    """
    Sets input parameters of program

    Args:
        memory_updates: A map of which places to update in memory
        memory: The RAM module to perform the updates in
    """
    for (index, new_value) in memory_updates.items():
        memory[index] = new_value
    return memory
