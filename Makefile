.PHONY : day
day: 
	cp -r aoc/day_0X aoc/day_`date +%d`
	cp tests/test_day_0X.py tests/test_day_0X.py
