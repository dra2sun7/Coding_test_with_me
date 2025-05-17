from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = cnt
                q.append((nx, ny, cnt+1))

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            graph[i][j] = 0
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            graph[i][j] = -1

for i in range(n):
    print(*graph[i])