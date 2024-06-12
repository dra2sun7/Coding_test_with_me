import sys
import heapq

N = int(input())
heap = []
answer = []

for i in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(heap, -x)
    else:
        if len(heap) == 0:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(heap))

for a in answer:
    print(a)