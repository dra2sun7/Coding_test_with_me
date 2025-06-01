import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx <= 0 or nx > n or ny <= 0 or ny > m:
            continue

        if graph[nx][ny] > 0:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                graph[x][y] += dfs(nx, ny)
    
    return graph[x][y]

n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]

visited = [[False]*(m+1) for _ in range(n+1)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

res = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if graph[i][j] != 0 and not visited[i][j]:
            visited[i][j] = True
            res = max(res, dfs(i, j))
print(res)