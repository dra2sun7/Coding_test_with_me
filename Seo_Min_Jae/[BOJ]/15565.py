from collections import Counter

n, k = map(int, input().split())
s = list(map(int, input().split()))

left = 0
counts = Counter()

res = float('inf')

for right in range(1, n+1):
    counts[s[right-1]] += 1
    
    if counts[1] >= k:
        while s[left] != 1:
            counts[s[left]] -= 1
            left += 1

        res = min(res, right-left)
    
        counts[s[left]] -= 1
        left += 1

if res == float('inf'):
    print(-1)
else:
    print(res)