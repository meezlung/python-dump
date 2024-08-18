# type: ignore

from operator import countOf
import re
needle = input()
haystack = input()
substringLen = len(needle)
count = 0

# there's plus 1 to not cut the last character in the sub string
# outputs the range of sub string
for i in range(len(haystack)-substringLen+1):
    # haystack index 0 to range of len of substring -> _ _ _ _ check 4 char ex: sses
    # assesses
    # ^--^
    #  ^--^ = pair to needle
    #   ^--^
    #    ^--^
    # ...
    #     ^--^ = pair
    # check every index if there's a match
    if haystack[i:i+substringLen] == needle: # determine if the needle length index matches with the needle word
        count+=1
print(count)
