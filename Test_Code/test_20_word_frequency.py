import importlib.util

spec = importlib.util.spec_from_file_location(
    "word_frequency",
    "Code/20_word_frequency.py"
)

module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert module.word_frequency("Python is easy Python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}

assert module.word_frequency("one two three") == {
    "one": 1,
    "two": 1,
    "three": 1
}

assert module.word_frequency("") == {}

print("All test cases passed.")