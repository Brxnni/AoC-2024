import re

import pathlib
LOCAL = pathlib.Path(__file__).parent
FILE = LOCAL / "input.txt"

with open(FILE, "r") as file:
	program = file.read()

def part1(p):
	pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
	instructions = re.findall(pattern, p)
	mul = lambda x,y:int(x)*int(y)
	return sum([ mul(*inst[4:-1].split(",")) for inst in instructions ])

def part2(p):
	pattern = re.compile(r"(?:mul\(\d{1,3},\d{1,3}\))|(?:do(?:n't)?\(\))")
	instructions = re.findall(pattern, p)
	final = 0
	do_status = True
	for inst in instructions:
		inst_type = inst.split("(")[0]
		if inst_type == "don't": do_status = False
		elif inst_type == "do": do_status = True
		elif inst_type == "mul" and do_status:
			x, y = inst[4:-1].split(",")
			final += int(x)*int(y)
	return final

print("P1 >>", part1(program))
print("P2 >>", part2(program))
