from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j, 0))
            visited[i][j] = True

while q:
    x, y, cnt = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if graph[nx][ny] == -1:
            continue

        if graph[nx][ny] == 0:
            if not visited[nx][ny]:
                graph[nx][ny] = 1
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

for i in range(n):
    if 0 in graph[i]:
        cnt = -1

print(cnt)

# cnt 제거
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        
        if graph[nx][ny] == -1:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        res = max(res, graph[i][j])

print(res - 1)