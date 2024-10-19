cases = int(input())

for i in range(cases):
    text = input().lower()
    count_dict = {}

    for char in text:
        if char.isalpha():
            count_dict[char] = count_dict.get(char, 0) + 1

    for char in count_dict:
        print(f"{char} = {count_dict[char]}")

    if i != cases - 1: print()