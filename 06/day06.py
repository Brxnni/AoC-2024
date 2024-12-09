import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		return [ line.strip() for line in file.readlines() ]

def part1(m):
	height, width = len(m), len(m[0])

	guard_position = [ (row_number, row.index("^")) for row_number, row in enumerate(m) if "^" in row ][0]
	directions = [(-1,0), (0,1), (1,0), (0,-1)]
	guard_direction = 0

	obstacles = [ (row_i, col_i) for col_i in range(width) for row_i in range(height) if m[row_i][col_i] == "#"  ]

	positions = set()
	while True:
		positions.add(guard_position)

		new_position = tuple([ sum(x) for x in zip(guard_position, directions[guard_direction]) ])
		if new_position not in obstacles:
			guard_position = new_position

			if not (0 <= guard_position[0] < height and 0 <= guard_position[1] < width):
				break
		else:
			guard_direction = (guard_direction + 1) % 4

	return len(positions)

if __name__ == "__main__":
    map_ = get_input("input")
    print("P1 >>", part1(map_))