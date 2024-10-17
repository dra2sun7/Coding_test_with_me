from collections import deque

N, M = map(int, input().split())
graph = []

for i in range(N):
    graph.append(input())
    if 'I' in graph[i]:
        x = i
        y = graph[i].index('I')

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        if x < 0 or x >= N or y < 0 or y >= M:
            continue

        if visited[x][y] == 1:
            continue

        visited[x][y] = 1

        if graph[x][y] == 'X':
            continue

        if graph[x][y] == 'P':
            answer += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            q.append((nx, ny))
    
    if answer == 0:
        answer = 'TT'

    return answer

print(bfs(x, y))