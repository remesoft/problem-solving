for _ in range(int(input())):
    p, q, c = map(int, input().split())
    result = pow(p, q, c) 
    print(f"Result = {result}")