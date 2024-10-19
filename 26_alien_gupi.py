for _ in range(int(input())):
    food = float(input())
    days = 0

    while food > 1.0:
        food /= 2.0
        days += 1

    print(f"{days} days")
