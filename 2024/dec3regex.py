from aocd import get_data, submit
import re

data = get_data(day=3, year=2024)

step1 = re.findall(r'''^.+?don't\(\)|do\(\).+?don't\(\)|do\(\).+$''', data, re.DOTALL)
print(len(step1))
step2 = []
for chunk in step1:
	step2 += re.findall(r'''mul\(\d+,\d+\)''', chunk)
total = 0
for mul in step2:
	temp = mul[4:-1].split(',')
	total += int(temp[0]) * int(temp[1])
print(total)
