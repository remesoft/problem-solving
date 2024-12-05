# https://codeforces.com/problemset/problem/231/A

count = 0

for _ in range(int(input())):

  if input().count("1") >= 2:
    count += 1

print(count)