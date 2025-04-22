from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt += 1
                    q.append((nx, ny))
    
    return cnt

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(bfs(i, j))
            count += 1

print(count)
for r in sorted(result):
    print(r)