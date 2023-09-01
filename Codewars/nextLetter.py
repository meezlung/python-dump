character = str(input("input: "))

order = ord(character)
if 65 <= order <= 89:
    order += 1
    converted = chr(order)
else:
    order = 65
    converted = chr(order)

print(converted)


