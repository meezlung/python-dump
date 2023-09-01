user = (input("ord/chr: "))

def checkUserInput(input):
    try:
        #convert to integer
        val = int(input)
        print(chr(val))
    except: ValueError
    try: 
        #convert to string
        val = str(input)
        print(ord(val))
    except: ValueError

checkUserInput(user)
