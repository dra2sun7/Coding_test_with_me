def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= r or ny < 0 or ny >= c:
             continue

        if graph[nx][ny] == '#':
            graph[nx][ny] = '.'
            dfs(nx, ny)


r, c = map(int, input().split())
graph = [list(input()) for _ in range(r)]
count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if graph[i][j] == '#':
            dfs(i, j)
            count += 1

print(count)