n = int(input())
for y_axis in range(0, n): # y axis
    X = 0
    for x_axis_number in range(y_axis, n): # x axis
        X = (X*10)+1 
    print(X)