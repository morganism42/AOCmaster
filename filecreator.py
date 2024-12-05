# Description: Creates a template file for each day of Advent of Code
def create_files(year, start=1, end=25):
	end += 1
	for day in range(start, end):
		filepath = f'C:\\Users\\liam\\Documents\\Python Scripts\\AOCmaster\\{year}\\dec{day}.py'
		with open(filepath, "w") as f:
			f.write(f'''from aocd import get_data, submit
def solve1(test=True):
    # Your solution code here
    testdata = \'\'\'\'\'\'
    testans = \'\'
    if test:
		data = testdata
	else:
		data = get_data(day={day}, year={year})
    
    
    
    
    
    
    if test and result == testans:
    	print("Test passed")
    elif test and result != testans:
		print("Test failed")
	elif not test:
		print(result)
        submit(result, part="a", day={day}, year={year})

''')
		f.close()
		print(f"Created {filepath}")
