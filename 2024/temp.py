for i in range(5, 26):
	filepath = 'C:\\Users\liam\Documents\Python Scripts\AOCmaster\\2024/dec' + str(i) + ".py"
	with open(filepath, "w") as f:
		f.write(f'''from aocd import get_data, submit

def solve(data):
    # Your solution code here
    pass

if __name__ == "__main__":
    data = get_data(day={i}, year=2024)
    result = solve(data)
    print(result)
    # submit(result, part="a", day=X, year=2024)''')
	f.close()
	print(f"Created {filepath}")
