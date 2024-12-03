from math import factorial
from collections import Counter

for _ in range(int(input())):
    n = input().split()
    word_count = len(n)
    freq = Counter(n)

    result = factorial(word_count)
    

    for count in freq.values():
        if count > 1:
            result //= factorial(count)
    
    print(f"1/{result}")