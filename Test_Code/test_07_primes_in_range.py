import importlib.util

spec = importlib.util.spec_from_file_location(
    "primes_in_range",
    "Code/07_primes_in_range.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.prime_numbers_in_range(1, 10) == [2, 3, 5, 7]
assert module.prime_numbers_in_range(10, 20) == [11, 13, 17, 19]
assert module.prime_numbers_in_range(20, 30) == [23, 29]
assert module.prime_numbers_in_range(1, 2) == [2]

print("All test cases passed.")