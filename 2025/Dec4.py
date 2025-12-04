from aocd import get_data

data = get_data(day=4, year=2025)

test = '''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.'''


def parser(Data):
	return [[1 if n == '@' else 0 for n in row] for row in Data.splitlines()]



def part1(Data):
	free = 0
	frees = []
	directions = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))
	for x, row in enumerate(Data):
		for y, column in enumerate(row):
			if Data[x][y] == 1:
				neighbours = 0
				for dx, dy in directions:
					if len(Data) > x + dx >= 0 and len(row) > y + dy >= 0:
						neighbours += Data[x + dx][y + dy]
				if neighbours < 4:
					free += 1
					frees.append((x, y))

	# print(free)
	return free, frees


def part2(Data):
	free = 0
	while True:
		newfree = 0
		directions = ((1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1))
		for x, row in enumerate(Data):
			for y, column in enumerate(row):
				if Data[x][y] == 1:
					neighbours = 0
					for dx, dy in directions:
						if len(Data) > x + dx >= 0 and len(row) > y + dy >= 0:
							neighbours += Data[x + dx][y + dy]
					if neighbours < 4:
						newfree += 1
						Data[x][y] = 0
		if newfree == 0:
			break
		free += newfree
	print(free)


data = parser(data)
part2(data)
