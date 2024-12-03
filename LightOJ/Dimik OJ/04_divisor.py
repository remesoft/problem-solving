for case in range(int(input())):
    number = int(input())
    divisior = []

    for count in range(1,number+1):
        if number % count == 0:
            divisior.append(str(count))

    print(f"Case {case + 1}: {' '.join(divisior)}")