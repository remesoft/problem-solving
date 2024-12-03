def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    armstrong_sum = sum([digit ** power for digit in digits])
    return armstrong_sum == n

for _ in range(int(input())):
    number = int(input())
    
    if is_armstrong(number):
        print(f"{number} is an armstrong number!")
    else:
        print(f"{number} is not an armstrong number!")
