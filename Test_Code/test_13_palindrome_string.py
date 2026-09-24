import importlib.util

spec = importlib.util.spec_from_file_location(
    "palindrome_string",
    "Code/13_palindrome_string.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") == True
assert module.is_palindrome_string("level") == True
assert module.is_palindrome_string("hello") == False
assert module.is_palindrome_string("python") == False
assert module.is_palindrome_string("racecar") == True

print("All test cases passed.")