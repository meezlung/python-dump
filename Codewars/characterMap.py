def char(a,b):    
    print("chr:  ", end="")
    for x in range(a,b):
        print(chr(x), end="   ")
    print("")
    print("asc: ", end="")
    for y in range(a,b):
        if len(str(y)) == 2:
            print(y, end="  ")
        else:
            print(y, end=" ")
    print("")

char(32,48)
char(48,64)
char(64,80)
char(80,96)
char(96,112)
char(112,128)