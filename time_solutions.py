import importlib.util
import inspect
import os
import re

import pathlib
LOCAL = pathlib.Path(__file__).parent

GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
END = "\033[0m"

import time

def get_solutions():
	solutions = {}

	for subdir, _, files in os.walk(LOCAL):
		for file in files:
			if re.match(r"^day\d+\.py$", file):
				file_path = os.path.join(subdir, file)
				module_name = os.path.splitext(os.path.relpath(file_path, LOCAL))[0].replace(os.sep, ".")
				spec = importlib.util.spec_from_file_location(module_name, file_path)
				module = importlib.util.module_from_spec(spec)
				spec.loader.exec_module(module)

				solutions[file.split(".")[0]] = dict(inspect.getmembers(module, inspect.isfunction))

	return solutions

# higher than 50 and the testing takes forever to run (python is slow yeah yeah stfu)
TRY_COUNT = 50

if __name__ == "__main__":
	all_functions = get_solutions()

	# To right-align all the function names across the entire output
	longest = max([ len(max(funcs.keys(), key=len)) for funcs in all_functions.values() ])

	for file, functions in all_functions.items():
		print(f"{BOLD}==== {file} ===={END}")
		inp = functions["get_input"]()

		times = {}
		for name, func in functions.items():
			if name == "get_input": continue
			# If we're currently doing part1_xyz, try checking for just part1
			comparison_time = times[name[:5]] if name[:5] in times.keys() else 0

			# Calculate average time it takes to run solution
			t0 = time.time()
			for _ in range(TRY_COUNT):
				res = func(inp)
			t1 = time.time()
			final = (t1-t0)/TRY_COUNT
			times[name] = final

			if comparison_time:
				diff = comparison_time / final
				diff_str = f"{RED}{round(1/diff, 2)}x slower{END}" if diff < 1 else f"{GREEN}{round(diff, 2)}x faster{END}"
				print(f"{(name):>{longest}} :: {BLUE}{(final):.4E}s{END} [{diff_str} than {name[:5]}]")
			else:
				print(f"{(name):>{longest}} :: {BLUE}{(final):.4E}s{END}")
