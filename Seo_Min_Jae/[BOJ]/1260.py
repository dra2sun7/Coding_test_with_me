from collections import defaultdict, deque

def dfs(node):
    if visited_dfs[node]:
        return
    
    visited_dfs[node] = True
    result_dfs.append(node)

    for d in sorted(graph[node]):
        if not visited_dfs[d]:
            dfs(d)

def bfs(node):
    q = deque([node])
    visited_bfs[node] = True

    while q:
        now = q.popleft()

        result_bfs.append(now)

        for b in sorted(graph[now]):
            if not visited_bfs[b]:
                visited_bfs[b] = True
                q.append(b)


n, m, v = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

result_dfs = []
dfs(v)
for d in result_dfs:
    print(d, end=' ')

print()

result_bfs = []
bfs(v)
for b in result_bfs:
    print(b, end=' ')