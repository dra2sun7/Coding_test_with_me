def dfs(node, count):
    if visited[node] != 0:
        return

    if not visited[node]:
        visited[node] = count
        dfs(graph[node], count + 1)

n, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(int(input()))
visited = [0] * n

dfs(0, 0)

if visited[k] != 0:
    print(visited[k])
else:
    print(-1)