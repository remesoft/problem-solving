for _ in range(int(input())):
    number = int(input())
    squareRoot = int(number ** 0.5)

    condition = squareRoot * squareRoot == number
    print("YES") if condition else print("NO")