def find_duplicates(numbers):
    duplicates = []
    seen = set()

    for number in numbers:
        if number in seen and number not in duplicates:
            duplicates.append(number)
        else:
            seen.add(number)

    return duplicates