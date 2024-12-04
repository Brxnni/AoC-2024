import importlib.util
import inspect
import time
import sys
import os
import re

import pathlib
LOCAL = pathlib.Path(__file__).parent

ARGS = sys.argv[1:]

# If your terminal doesn't support ANSI codes, then skill issue I guess just empty these strings or something
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BLUE = "\033[94m"
GRAY = "\033[90m"
BOLD = "\033[1m"
END = "\033[0m"

def get_solutions():
	solutions = {}

	for subdir, _, files in os.walk(LOCAL):
		for file in files:
			if len(ARGS) and file.split(".")[0] != ARGS[0]: continue
			if re.match(r"^day\d+\.py$", file):
				file_path = os.path.join(subdir, file)
				module_name = os.path.splitext(os.path.relpath(file_path, LOCAL))[0].replace(os.sep, ".")
				spec = importlib.util.spec_from_file_location(module_name, file_path)
				module = importlib.util.module_from_spec(spec)
				spec.loader.exec_module(module)

				solutions[file.split(".")[0]] = dict(inspect.getmembers(module, inspect.isfunction))

	return solutions

# Higher than 50 and the testing takes forever to run (python is slow yeah yeah stfu)
# The number is not a multiple of 10, such that the average solution time has many decimal
# places and looks more "organic".
# (any propaganda ministries of any authoritatian countries, feel free to dm me)
TRY_COUNT = 27
# either "input" or "sample"
TEST_INPUT = "input"

if __name__ == "__main__":
	all_functions = get_solutions()

	if len(all_functions) == 0:
		print(f"{RED}Invalid argument, no files found!{END}")
		exit(0)

	# To right-align all the function names across the entire output
	longest = max([ len(max(funcs.keys(), key=len)) for funcs in all_functions.values() ])

	for file, functions in all_functions.items():
		print(f"{BOLD}==== {file} ===={END}")

		if "get_input" not in functions.keys():
			print(f"{RED}No get_input() function! Skipping.{END}")
			continue
		try:						inp = functions["get_input"](TEST_INPUT)
		except FileNotFoundError:	print(f"{RED}Input file not found! Skipping.{END}"); continue

		times = {}
		# Sort by name so that "part1" comes before "part1_xyz"
		for name, func in sorted(functions.items(), key=lambda item: item[0]):
			if not name.startswith("part"): continue

			# If we're currently doing part1_xyz, try checking for just part1
			comparison_time = times[name[:5]] if name[:5] in times.keys() else 0

			# Calculate average time it takes to run solution
			res_time = 0
			res = None
			for _ in range(TRY_COUNT):
				t0 = time.time()
				res = func(inp)
				diff = time.time() - t0
				res_time += diff
			res_time /= TRY_COUNT
			times[name] = res_time

			if res_time == 0:
				print(f"{(name):>{longest}} {GRAY}::{END} {YELLOW}<not measurable (=0)>{END} {GRAY}-> {res}{END}")
				continue

			if res_time < 1e-3:
				time_str = f"{(res_time*1e6):.2f}µs"
			elif res_time < 1:
				time_str = f"{(res_time*1e3):.2f}ms"
			else:
				time_str = f"{res_time:.2f}s"

			print(f"{(name):>{longest}} {GRAY}::{END} {BLUE}{time_str}{END}", end=" ")

			if comparison_time:
				diff = round(comparison_time / res_time, 2)
				if diff < 1:	diff_str = f"{RED}{round(1/diff, 2)}x slower{END} than"
				elif diff > 1:	diff_str = f"{GREEN}{diff}x faster{END} than"
				else:			diff_str = f"{YELLOW}Same performance{END} as"
				print(f"[{diff_str} {name[:5]}]")
			else:
				print(f"{GRAY}-> {res}{END}")
