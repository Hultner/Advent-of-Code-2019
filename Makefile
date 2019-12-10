DAY := $(shell date +%d)

ifdef $$DAY
	DAY := $$DAY
endif

.PHONY : day
day: 
	cp -r aoc/day_0X aoc/day_$(DAY)
	cp tests/test_day_0X.py tests/test_day_$(DAY).py

build:
	rm aoc.o
	(cd aoc; zip -r -9 ../aoc.o .)
	chmod +x aoc.o
	ex -s -c '1i|#!/usr/bin/env python3' -c x aoc.o

