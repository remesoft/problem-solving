# https://vjudge.net/contest/676384#problem/F

def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def calculate_birthdays(d, m, y, qy):
    if m == 2 and d == 29:
        birthdays = 0
        for year in range(y + 1, qy + 1):
            if isLeapYear(year):
                birthdays += 1
        return birthdays
    else:
        return max(0, qy - y)

for case in range(1, int(input()) + 1):
    d, m, y, qy = map(int, input().split())
    birthdays = calculate_birthdays(d, m, y, qy)
    print(f"Case {case}: {birthdays}")