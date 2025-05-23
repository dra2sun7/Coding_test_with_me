import heapq
INF = int(1e9)

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    distance[x][y] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            
            if distance[nx][ny] > dist + graph[nx][ny]:
                distance[nx][ny] = dist + graph[nx][ny]
                heapq.heappush(q, (distance[nx][ny], nx, ny))

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    distance = [[INF]*n for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    dijkstra(0, 0)
    print(f"#{test_case} {distance[-1][-1]}")