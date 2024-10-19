alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

for _ in range(int(input())):
    text = input()
    numbers = []

    for char in text:
        index = alphabet.index(char) + 1
        numbers.append(str(index))

    print(''.join(numbers))