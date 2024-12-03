for _ in range(int(input())):
    r1, r2, B = map(int, input().split())

    if B == 0:
        currentRunRate = r2 / 50
    else:
        completedOver = (300 - B) / 6
        currentRunRate = r2 / completedOver

    if B == 0 or r2 > r1:
        requiredRunRate = 0.00
    else:
        runs_needed = (r1 + 1) - r2
        overs_remaining = B / 6
        requiredRunRate = runs_needed / overs_remaining

    print(f"{currentRunRate:.2f} {requiredRunRate:.2f}")