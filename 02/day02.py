import numpy as np

import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r") as file:
		return np.array([ list(map(int, line.strip().split(" "))) for line in file.readlines() ], dtype=np.object_)

def part1(m):
	diffs = [ np.diff(row) for row in m ]
	diffs = [ -diff if diff[0] < 0 else diff for diff in diffs ]
	diffs = list(map(lambda d: np.all(d > 0) and np.all(d <= 3), diffs))
	return diffs.count(True)

def part2(m):
	count = 0
	for row in m:
		# Stupid brute force solution:
		# Compute every variation of removing one level and check them all
		for i in range(len(row)):
			r = row.copy()
			r = np.delete(r, i)

			diff = np.diff(r)
			if diff[0] < 0: diff = -diff
			if np.all(diff > 0) and np.all(diff <= 3):
				count += 1
				break
	return count

def part2_earlycheck(m):
	count = 0

	def check(levels):
		diff = np.diff(levels)
		if diff[0] < 0: diff = -diff
		return np.all(diff > 0) and np.all(diff <= 3)

	for row in m:
		# Check before brute forcing
		if check(row):
			count += 1
			continue

		for i in range(len(row)):
			r = row.copy()
			r = np.delete(r, i)
			if check(r):
				count += 1
				break
	return count

if __name__ == "__main__":
	matrix = get_input()
	print("P1 >>", part1(matrix))
	print("P2 >>", part2(matrix))
