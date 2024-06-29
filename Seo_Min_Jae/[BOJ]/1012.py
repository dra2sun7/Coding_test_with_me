from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0

    while q:
        y, x = q.popleft()
    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                q.append((ny, nx))

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)]for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    answer = 0
    for yi  in range(n):
        for xi in range(m):
            if graph[yi][xi] == 1:
                bfs(yi, xi)
                answer += 1
    print(answer)

#################################################################################################
import sys
sys.setrecursionlimit(10000)

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    if graph[y][x] == 0:
        return
    
    graph[y][x] = 0
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<m and graph[ny][nx] == 1:
            dfs(ny, nx)


for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0 for _ in range(m)]for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    answer = 0
    for yi  in range(n):
        for xi in range(m):
            if graph[yi][xi] == 1:
                dfs(yi, xi)
                answer += 1
    print(answer)