n = int(input())
for x in range(1, n + 1):
    if n % x == 0:
        m = int(n/x)
        print("{} times {} equals {}".format(x,m,n))
