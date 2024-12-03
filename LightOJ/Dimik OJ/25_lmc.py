import math

for _ in range(int(input())):
    a, b = map(int, input().split())
    result = (a * b) // math.gcd(a, b)
    print(f"LCM = {result}")