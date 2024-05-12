import sys
import heapq

N = int(input())
heap = []
e = bool()

for i in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        e = False if x < 0 else True
        heapq.heappush(heap, (abs(x), e))
    else:
        if len(heap) == 0:
            print(0)
        else:
            x, e = heapq.heappop(heap)
            if e:
                print(x)
            else:
                print(-x)