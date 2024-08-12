# type: ignore

def isPalindrome(S):
    if S[::-1] == S[0:len(S)]: return True
    else: return False
print(isPalindrome('racecar'))