import re

import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r") as file:
		program = file.read().strip()

def part1(p):
	pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
	instructions = re.findall(pattern, p)
	mul = lambda x,y:int(x)*int(y)
	return sum([ mul(*inst[4:-1].split(",")) for inst in instructions ])

# Function without regex (7 times slower)
def part1_noregex(p):
	final = 0
	for i in range(len(p)):
		if p[i:i+4] == "mul(":
			sub = p[i+4:i+4+p[i+4:].index(")")]
			try:
				x, y = sub.split(",")
				x, y = int(x), int(y)
			except:	continue
			final += x*y
	return final

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

# Function without regex (10 times slower)
def part2_noregex(p):
	final = 0
	do_status = True
	for i in range(len(p)):
		if p[i:i+4] == "do()":		do_status = True
		if p[i:i+7] == "don't()":	do_status = False
		if p[i:i+4] == "mul(" and do_status:
			sub = p[i+4:i+4+p[i+4:].index(")")]
			try:
				x, y = sub.split(",")
				final += int(x) * int(y)
			except: ...
	return final

if __name__ == "__main__":
	program = get_input()
	print("P1 >>", part1(program))
	print("P2 >>", part2(program))
