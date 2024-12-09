from itertools import combinations

import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		return [ line.strip() for line in file.readlines() ]

class Vec:
	def __init__(self, a, b): self.a = a; self.b = b
	def __add__(self, other): return Vec(self.a+other.a, self.b+other.b)
	def __sub__(self, other): return Vec(self.a-other.a, self.b-other.b)
	def __eq__(self, other): return self.a == other.a and self.b == other.b
	def __hash__(self): return hash((self.a, self.b))
	def __repr__(self): return f"({self.a}, {self.b})"

def get_nodes(m):
	height, width = len(m), len(m[0])
	# Store antannae by type
	nodes = {}
	for ri in range(height):
		for ci in range(width):
			char = m[ri][ci]
			if char == ".": continue
			if char in nodes.keys(): nodes[char].append(Vec(ci, ri))
			else: nodes[char] = [Vec(ci, ri)]
	return nodes

def part1(m):
	height, width = len(m), len(m[0])
	nodes = get_nodes(m)

	def inside_bounds(loc): return 0 <= loc.a < width and 0 <= loc.b < height
	# Find antinodes: 2 per pair, 1 on either side
	locations = set()
	for coords in nodes.values():
		pairs = list(combinations(coords, 2))
		for pair in pairs:
			diff = pair[0] - pair[1]
			loc1 = pair[0] + diff
			loc2 = pair[1] - diff
			if inside_bounds(loc1): locations.add(loc1)
			if inside_bounds(loc2): locations.add(loc2)
	return len(locations)

def part2(m):
	height, width = len(m), len(m[0])
	nodes = get_nodes(m)

	def inside_bounds(loc): return 0 <= loc.a < width and 0 <= loc.b < height
	locations = set()
	for coords in nodes.values():
		for c in coords: locations.add(c)
		pairs = list(combinations(coords, 2))
		for pair in pairs:
			p1, p2 = pair
			diff = p1 - p2
			while True:
				p1 += diff
				if inside_bounds(p1): locations.add(p1)
				else: break
			while True:
				p2 -= diff
				if inside_bounds(p2): locations.add(p2)
				else: break
	return len(locations)
	
if __name__ == "__main__":
	antenna_map = get_input("input")
	print("P1 >>", part1(antenna_map))
	print("P2 >>", part2(antenna_map))
