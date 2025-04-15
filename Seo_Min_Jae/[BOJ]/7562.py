from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = True

    while q:
        x, y, cnt = q.popleft()

        if x == ex and y == ey:
            print(cnt)
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt+1))

t = int(input())
for _ in range(t):
    l = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited = [[False]*l for _ in range(l)]

    dx = [2, 2, -2, -2, -1, 1, -1, 1]
    dy = [-1, 1, -1, 1, 2, 2, -2, -2]

    bfs(sx, sy)