from collections import defaultdict, deque\

def bfs(x):
    q = deque([x])
    visited[x][x] = True

    while q:
        node = q.popleft()

        for j in graph[node]:
            if not visited[i][j]:
                q.append(j)
                visited[i][j] = True
                distance[i][j] = distance[i][node] + 1


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [[False]*(n+1) for _ in range(n+1)]
distance = [[0]*(n+1) for _ in range(n+1)]

result = []

for i in range(1, n+1):
    bfs(i)
    result.append(sum(distance[i]))

print(result.index(min(result))+1)