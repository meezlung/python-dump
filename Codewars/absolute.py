x=int(input())
if x >= 0:
   print(x)
else:
   x = str(x)
   y = x.replace('-', '')
   print(y)