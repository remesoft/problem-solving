# https://codeforces.com/problemset/problem/158/A


# Input parsing
n, k = map(int, input().split())
scores = list(map(int, input().split()))

# Threshold score
threshold = scores[k-1]

# Count how many participants advance
advancers = 0
for score in scores:
    if score >= threshold and score > 0:
        advancers += 1

# Output the result
print(advancers)




