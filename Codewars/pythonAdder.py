s = input()
# takes the input
index = s.find('+')

# removes + in the list
for position in range(0, len(s)):
    if position == index:
        continue
    # gets the index of the numbers before and after the index of '+'
    # then gets the sum
    sum = int(s[:index]) + int(s[index:])
print(sum)