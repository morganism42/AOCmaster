# Description: Creates a template file for each day of Advent of Code
def create_files(year, start=1, end=25):
	end += 1
	for day in range(start, end):
		filepath = f'C:\\Users\\liam\\Documents\\Python Scripts\\AOCmaster\\{year}\\dec{day}.py'
		with open(filepath, "w") as f:
			f.write(f'''from aocd import get_data, submit
def solve(data):
    # Your solution code here
    pass

if __name__ == "__main__":
    data = get_data(day={day}, year=2024)
    result = solve(data)
    print(result)
    # submit(result, part="a", day=X, year={year})''')
		f.close()
		print(f"Created {filepath}")
