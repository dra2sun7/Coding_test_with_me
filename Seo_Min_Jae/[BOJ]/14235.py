import heapq

n = int(input())
heap = []
answer = []

for i in range(n):
    a = list(map(int, input().split()))
    a, nums = a[0], a[1:]

    for i in range(a):
        heapq.heappush(heap, -nums[i])

    if a == 0:
        if not heap:
            answer.append(-1)
        else:
            answer.append(-heapq.heappop(heap))

for ans in answer:
    print(ans)