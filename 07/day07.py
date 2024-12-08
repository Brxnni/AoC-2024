import pathlib
LOCAL = pathlib.Path(__file__).parent

def get_input(input_type = "input"):
	with open(LOCAL / f"{input_type}.txt", "r", encoding="utf-8") as file:
		return [(
			int(line.split(": ")[0]),
			list(map(int, line.strip().split(": ")[1].split(" ")))
		) for line in file.readlines()]

def part1(n):
	count = 0
	def check(res, nums):
		if len(nums) == 1:
			return nums[0] == res

		# + or *
		return check(res - nums[-1], nums[:-1]) or check(res / nums[-1], nums[:-1])

	for line in n:
		if check(*line): count += line[0]
	return count

# Checks if the division would result in a float before calling the function recursively
def part1_earlycheck(n):
	count = 0
	def check(res, nums):
		if len(nums) == 1:
			return nums[0] == res

		if check(res - nums[-1], nums[:-1]): return True
		if res % nums[-1] == 0:
			if check(int(res / nums[-1]), nums[:-1]): return True

		return False

	for line in n:
		if check(*line): count += line[0]
	return count

def part2(n):
	count = 0
	def check(res, nums):
		if len(nums) == 1:
			return nums[0] == res

		# + operator
		if check(res - nums[-1], nums[:-1]):
			return True
		# * operator
		if res % nums[-1] == 0:
			if check(int(res / nums[-1]), nums[:-1]): return True
		# || operator
		if str(res).endswith(str(nums[-1])):
			try:
				if check(int(str(res)[:-len(str(nums[-1]))]), nums[:-1]): return True
			except: ...

		return False

	for line in n:
		if check(*line): count += line[0]
	return count

if __name__ == "__main__":
	n = get_input("input")
	print("P1 >>", part1(n))
	print("P2 >>", part2(n))
