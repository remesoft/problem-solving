for _ in range(int(input())):
    number = input()

    first_number = int(number[0])
    last_number = int(number[len(number) - 1])
    sum = first_number + last_number

    print(f"Sum = {sum}")
    