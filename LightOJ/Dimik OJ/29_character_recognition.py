for _ in range(int(input())):
    char = input().strip()

    if char.isupper():
        print("Uppercase Character")
    elif char.islower():
        print("Lowercase Character")
    elif char.isdigit():
        print("Numerical Digit")
    else:
        print("Special Characters")
