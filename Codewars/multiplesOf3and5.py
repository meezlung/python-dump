def solution(number):
    # sum = 0

    # for i in range(number):
    #     if i % 3 == 0 or i % 5 == 0:
    #         sum += i

    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0) # short solution

print(solution(4))
print(solution(6))
print(solution(16))
print(solution(8)) # == 8
print(solution(10)) # == 23
