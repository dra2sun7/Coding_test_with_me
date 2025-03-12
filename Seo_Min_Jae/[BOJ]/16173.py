def dfs(x, y):
    if x < 0  or x >= n or y < 0 or y >= n:
        return
    
    if visited[x][y] == False:
        visited[x][y] = True

        for i in range(2):
            nx = x + dx[i] * graph[x][y]
            ny = y + dy[i] * graph[x][y]

            dfs(nx, ny)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

dx = [0, 1]
dy = [1, 0]

dfs(0, 0)

if visited[n-1][n-1]:
    print("HaruHaru")
else:
    print("Hing")
