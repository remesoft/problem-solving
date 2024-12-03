import math


for _ in range(int(input())):
    number = int(input())

    if number <= 1 : break

    divisors_sum = 1
    sqrt_number = int(math.sqrt(number))

    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i


def is_perfect_number(n):
    if n <= 1:
        return False
    divisors_sum = 1
    sqrt_n = int(math.sqrt(n))

    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i

    return divisors_sum == n

for _ in range(int(input())):
    number = int(input())
    
    if is_perfect_number(number):
        print(f"YES, {number} is a perfect number!")
    else:
        print(f"NO, {number} is not a perfect number!")
