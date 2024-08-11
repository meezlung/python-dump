# type: ignore

text = "The sunset sets at twelve o' clock."

def alphabet_position(text):
    # Initialize
    txt = []

    # Make all char lower to filter and limit ASCII
    for char in text.lower():
        # Convert the text into ASCII 
        # Since we're in all lower case, we all get the same results and we can safely subtract 96
        conv = txt.append(ord(char)-96)
        # But if there's a negative number in txt, we remove it from the Initialized variable
        for conv in txt:
            if conv < 0:
                txt.remove(conv)
    # Convert list to string and remove all commas
    return " ".join(str(char) for char in txt)
print(alphabet_position(text))