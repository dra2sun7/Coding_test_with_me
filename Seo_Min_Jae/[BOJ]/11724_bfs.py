from collections import defaultdict, deque
import sys

input = sys.stdin.readline

def bfs(node):
    q = deque([node])
    visited[node] = True

    while q:
        now = q.popleft()

        for x in graph[now]:
            if not visited[x]:
                visited[x] = True
                q.append(x)


n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
count = 0

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        count += 1

print(count)