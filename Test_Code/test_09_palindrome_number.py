import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_number",
    "Code/09_palindrome_number.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_number(121) == True
assert module.is_palindrome_number(1221) == True
assert module.is_palindrome_number(123) == False
assert module.is_palindrome_number(10) == False
assert module.is_palindrome_number(7) == True

print("All test cases passed.")