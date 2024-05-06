import heapq

N = int(input())
heap = []
answer = 0

for i in range(N):
    n = int(input())
    if i == 0:
        ds_n = n
    else:
        heapq.heappush(heap, (-n, i+1))

if not heap:
    pass
else:
    while ds_n <= -heap[0][0]:
        n, i = heapq.heappop(heap)
        heapq.heappush(heap, (n+1, i))
        ds_n += 1
        answer += 1

print(answer)