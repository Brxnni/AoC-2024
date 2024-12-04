import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		return [ line.strip() for line in file.readlines() ]

def part1(text):
	rows = text
	columns = [ "".join(row) for row in list(zip(*text)) ]
	diagonal_coords = []
	dim = len(text)
	if dim > 4:
		diagonal_coords.append([ (i,i) for i in range(dim) ])
		diagonal_coords.append([ (dim-i-1, i) for i in range(dim) ])

	extras = dim - 4
	for j in range(1, extras+1):
		diagonal_coords.append([ (i,i+j) for i in range(dim-j) ])
		diagonal_coords.append([ (i+j,i) for i in range(dim-j) ])
		diagonal_coords.append([ (dim-i-1,i+j) for i in range(dim-j) ])
		# diagonal_coords.append([ (i+j,dim-i-1) for i in range(dim-j+1) ])
	diagonals = [ "".join([ text[d[1]][d[0]] for d in diagonal ]) for diagonal in diagonal_coords ]

	[ print(l) for l in list(zip([(dc[0],dc[-1]) for dc in diagonal_coords], diagonals))]

	c = lambda ts: sum([ t.count("XMAS") for t in ts ]) + sum([ t[::-1].count("XMAS") for t in ts ])
	return c(rows) + c(columns) + c(diagonals)

if __name__ == "__main__":
	puzzle = get_input("sample")
	print("P1 >>", part1(puzzle))
	# print("P2 >>", part2(puzzle))
