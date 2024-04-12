user = (input("ord/chr: "))

def checkUserInput(input):
    try:
        #convert to integer
        val = int(input)
        print(chr(val))
    except: 
        raise ValueError
    try: 
        #convert to string
        val = str(input)
        print(ord(val))
    except: 
        raise ValueError

checkUserInput(user)
