import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		parts = [ part.split("\n") for part in file.read().split("\n\n") ]
		return (
			[list(map(int, row.split("|"))) for row in parts[0]],
			[list(map(int, row.split(","))) for row in parts[1]]
		)

def part1(program):
	rules, pagelists = program
	total = 0
	for pages in pagelists:
		correct = True

		for i in range(len(pages)):
			num, after = pages[i], pages[i+1:]
			correct &= all([ [num, a] in rules for a in after ])

		if correct:
			total += pages[len(pages)//2]

	return total

def part2(program):
	rules, pagelists = program

if __name__ == "__main__":
	p = get_input("input")
	print("P1 >>", part1(p))
	# print("P2 >>", part2(rules, pages))
