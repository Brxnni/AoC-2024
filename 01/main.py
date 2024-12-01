import numpy as np

import pathlib
LOCAL = pathlib.Path(__file__).parent
FILE = LOCAL / "input.txt"

with open(FILE, "r") as file:
	mat = np.array([ list(map(int, line.strip().split("   "))) for line in file.readlines() ])

def part1(m):
	m = np.transpose(m)
	m.sort(axis=1)
	return sum(np.absolute(m[1] - m[0]))

def part2(m):
	m = np.transpose(m)
	occ = dict(zip(*np.unique(m[1], return_counts=True)))
	return sum([ n * occ.get(n, 0) for n in m[0] ])

print("P1 >>", part1(mat))
print("P2 >>", part2(mat))
