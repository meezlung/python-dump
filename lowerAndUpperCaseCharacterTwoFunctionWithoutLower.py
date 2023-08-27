def lowerChar(char):
    order = ord(char)
    if 65 <= order <= 91:
        order += 32
        return chr(order)
    else:
        return chr(order)

def lowerString(string):
    result = ''
    for i in range(len(string)):
        result += lowerChar(string[i])
    return result

# made a shorter code

def upperString(string):
    result = ""
    for i in range(len(string)):
        order = ord(string[i])
        if 97 <= order <= 122:
            order -= 32
            result += chr(order)
        else:
            result += chr(order)
    return result
                  

print(lowerString('AbC!'))
print(upperString("aBc!"))