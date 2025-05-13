from collections import deque

def bfs(s):
    q = deque()
    q.append((s, 0))
    visited[s] = True

    while q:
        floor, cnt = q.popleft()

        if floor == G:
            return cnt
        
        if floor + U <= F and not visited[floor+U]:
            visited[floor+U] = True
            q.append((floor+U, cnt+1))
        
        if floor - D > 0 and not visited[floor-D]:
            visited[floor-D] = True
            q.append((floor-D, cnt+1))
    
    return -1


F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)

res = bfs(S)

if res == -1:
    print("use the stairs")
else:
    print(res)