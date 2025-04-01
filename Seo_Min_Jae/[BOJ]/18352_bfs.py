from collections import defaultdict, deque
import sys

def bfs(node):
    q = deque([node])
    visit[node] = True
    distance[node] = 0

    while q:
        now = q.popleft()

        for v in graph[now]:
            if not visit[v]:
                visit[v] = True
                distance[v] = distance[now] + 1
                q.append(v)


n, m, k, x = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visit = [False] * (n+1)
distance = [0] * (n+1)

bfs(x)

if k in distance:
    for i, v in enumerate(distance):
        if v == k:
            print(i)
else:
    print(-1)