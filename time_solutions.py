import importlib.util
import inspect
import os
import re

import pathlib
LOCAL = pathlib.Path(__file__).parent

class C:
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

				solutions[module_name] = dict(inspect.getmembers(module, inspect.isfunction))

				# Get functions defined in the module
				# for name, func in inspect.getmembers(module, inspect.isfunction):
					# Store the function in the dictionary
					# solutions[name] = func

	return solutions

TRY_COUNT = 50

if __name__ == "__main__":
	all_functions = get_solutions()
	
	longest = max([ len(max(funcs.keys(), key=len)) for funcs in all_functions.values() ])

	for file, functions in all_functions.items():
		print(f"{C.BOLD}==== {file} ===={C.END}")
		inp = functions["get_input"]()

		times = {}
		for name, func in functions.items():
			if name == "get_input": continue
			comparison_time = times[name[:5]] if name[:5] in times.keys() else 0

			t0 = time.time()
			for _ in range(TRY_COUNT):
				res = func(inp)
			t1 = time.time()
			final = (t1-t0)/TRY_COUNT
			times[name] = final

			if comparison_time:
				diff = comparison_time / final
				diff_str = f"{C.RED}{round(1/diff, 2)}x slower{C.END}" if diff < 1 else f"{C.GREEN}{round(diff, 2)}x faster{C.END}"
				print(f"{(name):>{longest}} :: {C.BLUE}{(final):.4E}s{C.END} [{diff_str} than {name[:5]}]")
			else:
				print(f"{(name):>{longest}} :: {C.BLUE}{(final):.4E}s{C.END}")
