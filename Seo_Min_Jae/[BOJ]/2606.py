from collections import defaultdict, deque

n = int(input())
m = int(input())
dict = defaultdict(list)

for _ in range(m):
    k, v = map(int, input().split())
    dict[k].append(v)
    dict[v].append(k)

def bfs(x):
    q = deque()
    visited = [0 for _ in range(n+1)]
    q.append(x)
    visited[x] = 1

    while q:
        y = q.popleft()
        
        for i in dict[y]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    
    return visited.count(1)-1

print(bfs(1))