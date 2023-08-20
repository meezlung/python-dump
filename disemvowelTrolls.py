def disemvowel(string_):
    for char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        if char in string_: string_=string_.replace(char, "")
    return string_

print(disemvowel("This website is for losers LOL!"))