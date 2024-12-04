import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		return [ line.strip() for line in file.readlines() ]

def part1(text):
	rows = text
	columns = [ "".join(row) for row in list(zip(*text)) ]
	diagonal_coords = []
	# The input is square shaped!!!!! this will prevent the second bronze age collapse
	size = len(text)

	# NW/SE diagonals (only the ones of length at least 4)
	diagonal_coords.append([ (c,c) for c in range(size) ])
	for i in range(1, size-4+1):
		diagonal_coords.append([ (i+j,j) for j in range(size-i) ])
		diagonal_coords.append([ (j,i+j) for j in range(size-i)  ])

	# NE/SW diagonals
	diagonal_coords.append([ (size-1-c,c) for c in range(size) ])
	for i in range(1, size-4+1):
		diagonal_coords.append([ (size-1-i-j,j) for j in range(size-i) ])
		diagonal_coords.append([ (size-1-j,i+j) for j in range(size-i) ])

	diagonals = [ "".join([ text[d[1]][d[0]] for d in diagonal ]) for diagonal in diagonal_coords ]
	count = lambda texts: sum([ t.count("XMAS") for t in texts ]) + sum([ t[::-1].count("XMAS") for t in texts ])

	return count(rows) + count(columns) + count(diagonals)

if __name__ == "__main__":
	puzzle = get_input("input")
	print("P1 >>", part1(puzzle))
	# print("P2 >>", part2(puzzle))
