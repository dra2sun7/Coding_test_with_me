from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((0,0))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if xx < 0 or xx >= n or yy < 0 or yy >= m:
                continue
            if maps[xx][yy] == 0:
                continue
            if maps[xx][yy] == 1:
                maps[xx][yy] = maps[x][y] + 1
                q.append((xx, yy))
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]