def duplicate_count(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count

print(duplicate_count('aabbcdae'))     