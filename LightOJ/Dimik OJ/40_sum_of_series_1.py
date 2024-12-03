T = int(input())

for _ in range(T):
    X, K = map(int, input().split())

    result = sum(X ** i for i in range(K + 1))
    print(f"Result = {result}")
