from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))

    while q:
        num, cnt = q.popleft()

        if num > b:
            continue

        if num == b:
            print(cnt + 1)
            return

        q.append((num*2, cnt+1))
        q.append((int(str(num)+"1"), cnt+1))
    
    print(-1)

a, b = map(int, input().split())
bfs(a)