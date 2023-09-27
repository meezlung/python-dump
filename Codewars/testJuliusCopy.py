while True:
    condition = input('may tanong ka ba tangina ka: ')

    if condition == 'y':
        operation = input('ano tanong mo : ').split()
        x = int(operation[0])
        y = int(operation[2])
        operator = operation[1]

        if operator == '+':
            print(x + y)

        elif operator == '-':
            print(x - y)

        elif operator == '/':
            print(x / y)

        elif operator == '*':
            print(x * y)

        else:
            print('bobo mali')
            continue

    elif condition == 'n':
        print('ok')
        break

    else:
        print('mali tanga')
        continue