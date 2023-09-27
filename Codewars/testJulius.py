num1 = int(input("Enter First Number:"))
ope = (input("Enter Operator:"))
num2 = int(input("Enter Second Number:"))

if ope=="+":
    print("{} + {} =".format(num1, num2), num1+num2)
elif ope=="-":
    print("{} - {} =".format(num1, num2), num1-num2)
elif ope=="*":
    print("{} * {} =".format(num1, num2), num1*num2)
elif ope=="/":
    if num2 == 0 :
        print("Division by 0 is not allowed")
    else: 
        print("{} / {} =".format(num1, num2), num1/num2)
elif ope=="%":
    if num2 == 0 :
        print("Modulo by 0 is not allowed")
    else: 
        print("{} % {} =".format(num1, num2), num1%num2)
else :
    print("Invalid Operator")
    
numn = str(input("Enter another number? Y/N: "))
numn = numn.upper()

while numn == "N":
    print("Thank you for using the calculator!")
    break

while numn != "Y" and numn != "N":
    print(numn, "Is an invalid input, try again")
    numn = str(input("Enter another number? Y/N: "))
    numn = numn.upper()
    if numn == "N":
        print("Thank you for using the calculator!")
        break
    elif numn == "Y":
        numn = "Y"

while numn == "Y":
        numn1 = int(input("Enter Another Number:"))
        ope1 = (input("Enter Operator:"))
        numn2 = int(input("Enter Another Number:"))
        if ope1=="+":
            print("{} + {} =".format(numn1, numn2), numn1+numn2)
        elif ope1=="-":
            print("{} - {} =".format(numn1, numn2), numn1-numn2)
        elif ope1=="*":
            print("{} * {} =".format(numn1, numn2), numn1*numn2)
        elif ope1=="/":
            if numn2 == 0:
                print("Division by 0 is not allowed")
            else:
                print("{} / {} =".format(numn1, numn2), numn1/numn2)
        elif ope1=="%":
             if numn2 == 0:
                print("Modulo by 0 is not allowed")
             else:
                print("{} % {} =".format(numn1, numn2), numn1%numn2)
        else:
            print("Invalid Operator")
        numn = str(input("Enter another number? Y/N: "))
        numn = numn.upper()
        if numn == "N":
            print("Thank you for using the calculator!")
            break