# https://codeforces.com/problemset/problem/71/A

for _ in range(int(input())):
  word = input()
  length = len(word)
  
  if len(word) > 10:
    print(f"{word[0]}{length-2}{word[length-1]}")
  else:
    print(word)