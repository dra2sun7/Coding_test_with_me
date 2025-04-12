import heapq

def dijkstra(cnt, x):
    q = []
    heapq.heappush(q, (-x, cnt))

    while q:
        now, dist = heapq.heappop(q)
        now = -now

        if now > b:
            continue

        if now == b:
            print(dist+1)
            return

        # 곱하기 2
        heapq.heappush(q, (-(now*2), dist+1))

        # 1 추가
        heapq.heappush(q, (-(int(str(now)+"1")), dist+1))
    
    print(-1)

a, b = map(int, input().split())
dijkstra(0, a)