for i in range(int(input())):
    numbers = input().split()
    sorted_numbers = ' '.join(sorted(numbers, key=int))
    print(f"Case {i+1}: {sorted_numbers}")