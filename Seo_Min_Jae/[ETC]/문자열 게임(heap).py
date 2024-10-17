import heapq
from collections import Counter

s = 'aabcbcbcabcc'
k = 3

answer = 0

dict = Counter(s)
heap = []

for s, n in dict.items():
    heapq.heappush(heap, (-n, s))

for i in range(k):
    x = heapq.heappop(heap)
    if x[0] == -1:
        pass
    else:
        heapq.heappush(heap, (x[0]+1, x[1]))

for h in heap:
    n, s = h
    answer += n**2

print(answer)