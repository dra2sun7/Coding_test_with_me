import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    visited[x][y] = True

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] > k:
            if not visited[nx][ny]:
                dfs(nx, ny)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_length = 0
for i in range(n):
    max_length = max(max_length, max(graph[i]))

answer = 0
for k in range(0, max_length+1):
    visited = [[False]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                dfs(i, j)
                cnt += 1 
    answer = max(answer, cnt)

print(answer)