# negative checker
# strictly small checker
# a + b + c = d
# len(a) = len(b) = len(c)

def decompose(d: int) -> tuple[int, int, int] | None:
    
    for i in range(d):
        if (d - i) % 3 == 0:
            ans = (d - i) // 3
            x = ans
            y = x + 1
            z = (i - 1) + x

            if x + y + z == d and len(str(x)) == len(str(y)) == len(str(z)) and x < y < z:
                return (x, y, z)
            
    return None
    
# print(decompose(6))
# print(decompose(8000))
# print(decompose(10))
# print(decompose(100))