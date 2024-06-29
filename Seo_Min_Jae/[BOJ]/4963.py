from collections import deque
import sys
input = sys.stdin.readline

def bfs(i, j):
    dx = [-1, -1, 0, 1, 1, 1, 0 , -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    q = deque()
    q.append((i, j))
    graph[x][y] = 0   #20번째 줄 추가하며 while 밖으로 뺌

    while q:
        x, y = q.popleft()
        
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny] == 1:
                graph[nx][ny] = 0   # 얘 때문에 계속 시간초과 뜸. 얘 추가해줘야 함.
                q.append((nx, ny))

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                answer += 1
    print(answer)