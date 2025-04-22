def dfs(x, y):
    visited[x][y] = True
    size = 1

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 1:
            if not visited[nx][ny]:
                size += dfs(nx, ny)
    
    return size

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            result.append(dfs(i, j))

print(len(result))
for r in sorted(result):
    print(r)