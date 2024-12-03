for _ in range(int(input())):
    arr = list(map(int, input().split()))
    alternate_elements = arr[1::2]
    
    print(" ".join(map(str, alternate_elements)))