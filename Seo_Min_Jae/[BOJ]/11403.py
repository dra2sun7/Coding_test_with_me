from collections import deque
import collections

def bfs(x):
    q = deque([x])

    while q:
        node = q.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    
    result.append(visited)

n = int(input())
lists = [list(map(int, input().split())) for _ in range(n)]

graph = collections.defaultdict(list)

for i in range(n):
    for j in range(n):
        if lists[i][j] == 1:
            graph[i].append(j)

result = []

for i in range(n):
    visited = [0] * n
    bfs(i)

for i in range(n):
    for j in range(n):
        print(result[i][j], end =' ')
    print()