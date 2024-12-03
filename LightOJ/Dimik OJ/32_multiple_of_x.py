cases = int(input())

for T in range(cases):
    X, N = map(int, input().split())
    print(X)

    if X > N:
        print("Invalid!")
    else:
        for multiple in range(X, N + 1, X):
            print(multiple)


    if T < cases - 1:
        print()
