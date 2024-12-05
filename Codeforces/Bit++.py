# https://codeforces.com/problemset/problem/282/A

value = 0

for _ in range(int(input())):
  
  if input().count("++"):
    value += 1
  else:
    value -= 1
    

print(value)

