cases = int(input())

for t in range(cases):
    n = int(input())
    stars = n * n

    for star in range(1, stars + 1):
        print("*", end="")
        if star % n == 0:
            print() 

    if t != cases - 1: print()
        
        
