from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    width = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    width += 1
    
    return width

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
max_width = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            max_width = max(max_width, bfs(i, j))
            cnt += 1

print(cnt)
print(max_width)