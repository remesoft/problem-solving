import math
import re

for _ in range(int(input())):
    factorial = str(math.factorial(int(input())))
    match = re.search(r'0+$', factorial)
    last_zeros = len(match.group(0)) if match else 0
    print(last_zeros)
