from collections import defaultdict
import sys

sys.setrecursionlimit(10**6) #런타임에러 방지
input = sys.stdin.readline #시간초과 방지

def dfs(node):
    visited[node] = True

    for x in graph[node]:
        if not visited[x]:
            dfs(x)

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
        dfs(i)
        count += 1

print(count)