# https://vjudge.net/contest/676384#problem/G

specials = [1, 64, 729, 4096, 15625, 46656, 117649, 262144, 531441,
1000000, 1771561, 2985984, 4826809, 7529536, 11390625, 16777216, 24137569, 34012224,
47045881, 64000000, 85766121]


while True:
  number = int(input())
  if number == 0 : break
  print("Special" if number in specials else "Ordinary")

