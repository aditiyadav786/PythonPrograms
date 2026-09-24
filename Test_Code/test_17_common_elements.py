import importlib.util

spec = importlib.util.spec_from_file_location(
    "common_elements",
    "Code/17_common_elements.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert module.common_elements([1, 2, 3], [4, 5, 6]) == []
assert module.common_elements([1, 2, 2, 3], [2, 3]) == [2, 2, 3]
assert module.common_elements([], [1, 2]) == []

print("All test cases passed.")