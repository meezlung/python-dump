# x = int(input())
# dict = {1: '1st', 2: '2nd', 3: '3rd', 4: '4th', 5: '5th', 6: '6th', 7: '7th', 8: '8th', 9: '9th'}
# print(dict[x])

x = int(input())

if x == 1: print("{}st".format(x))
elif x == 2: print("{}nd".format(x))
elif x == 3: print("{}rd".format(x))
else: print("{}th".format(x))