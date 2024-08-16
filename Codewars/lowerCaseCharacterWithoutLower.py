# type: ignore

def lowerChar(char):
    empty = ""
    for o in char:
        order = ord(o)
        if 65 <= order <= 91:
            empty += chr(order+32)
        else:
            empty += chr(order)
    return(empty)