def naturalNumbers(n):
    numbers = []
    for i in range(1,n+1):
        numbers.append(i)
    return ', '.join(map(str, numbers))

print(naturalNumbers(50))