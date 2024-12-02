import numpy as np

import pathlib
LOCAL = pathlib.Path(__file__).parent
FILE = LOCAL / "input.txt"

with open(FILE, "r") as file:
	mat = np.array([ list(map(int, line.strip().split(" "))) for line in file.readlines() ], dtype=np.object_)

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

print("P1 >>", part1(mat))
print("P2 >>", part2(mat))
