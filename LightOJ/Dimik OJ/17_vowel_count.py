import re

for _ in range(int(input())):
    sentence = input()
    vowels = re.findall(r'[aeiouAEIOU]', sentence)
    print(f"Number of vowels = {len(vowels)}")