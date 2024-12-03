import numpy as np

import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r") as file:
		return np.array([ list(map(int, line.strip().split("   "))) for line in file.readlines() ])

def part1(m):
	m = np.transpose(m)
	m.sort(axis=1)
	return sum(np.absolute(m[1] - m[0]))

def part2(m):
	m = np.transpose(m)
	occ = dict(zip(*np.unique(m[1], return_counts=True)))
	return sum([ n * occ.get(n, 0) for n in m[0] ])

if __name__ == "__main__":
	matrix = get_input()
	print("P1 >>", part1(matrix))
	print("P2 >>", part2(matrix))
