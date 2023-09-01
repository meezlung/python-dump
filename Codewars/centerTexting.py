import math

width = int(input())
text = []
while True:
    THEinput=input("")
    if THEinput=="END":
        break
    else:
        text.append(THEinput)
for x in text:
    print((((math.ceil(width/2)-math.floor(len(x)/2)))*".")+x+(((math.floor(width/2))-math.ceil(len(x)/2))*"."))