from time import time

# https://docs.google.com/spreadsheets/d/1KTNHbQg4-Z2twP5IhQFCPmNuM9DqJBZ0ytfh877wiBY/edit#gid=847833676

def slow_sum(k):
    sum = 0
    for i in range(k):
        sum += i + 1
    return sum 

def slow_space_sum(k):
    numbers = []
    for i in range(k):
        numbers.append(i + 1)
    return sum(numbers)

def fast_sum(k):
    return k * (1 + k) // 2

def run_sum(f, k):
    start_time = time()
    f(k)
    end_time = time()
    return (end_time - start_time) * 1000

def main():
    for i in range(1000000, 10000000, 1000000):
        all_runtimes = 0
        for j in range(100): # 10 times natin makukuha ung time per 1000000
            all_runtimes += run_sum(fast_sum, i)
        print(i, all_runtimes/100)

        # print(i, run_sum(slow_space_sum, i))
        # print(i, run_sum(fast_sum, i))

if __name__ == "__main__":
    main() 