import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, allied):
    cnt = 1

    if graph[x][y] != allied:
        return 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if graph[nx][ny] == allied:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += dfs(nx, ny, allied)
    
    return cnt


m, n = map(int, input().split())
graph = [list(input()) for _ in range(n)]

visited = [[False]*m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

white = blue = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W' and not visited[i][j]:
            visited[i][j] = True
            w = dfs(i, j, 'W')
            white += w**2

        elif graph[i][j] == 'B' and not visited[i][j]:
            visited[i][j] = True
            b = dfs(i, j, 'B')
            blue += b**2

print(white, blue)