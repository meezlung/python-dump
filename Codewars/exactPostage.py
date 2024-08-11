# type: ignore

def postalValidate(S):
    new_S = S.replace(' ', '') # remove spaces
    if len(new_S) == 6:
        if new_S[0:7:2].isalpha() and new_S[1:7:2].isdigit():
            return new_S.upper()
        else: return False
    else: return False
print(postalValidate('  d3  L3  T3'))

