import importlib.util

spec = importlib.util.spec_from_file_location(
    "missing_number",
    "Code/18_missing_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_missing_number([1, 2, 3, 5]) == 4
assert module.find_missing_number([1, 2, 4, 5]) == 3
assert module.find_missing_number([2, 3, 4, 5]) == 1
assert module.find_missing_number([1, 3, 4, 5]) == 2

print("All test cases passed.")