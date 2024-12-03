for _ in range(int(input())):
    array = input().split()
    sorted_array = sorted(array)
    print("YES" if array == sorted_array else "NO")