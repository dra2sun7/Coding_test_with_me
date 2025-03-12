def dfs(index, count):
    if visited[index] != 0:
        return 
    
    if visited[index] == 0:
        visited[index] = count
        count += 1

        dfs(graph[index]-1, count)


t = int(input())

for _ in range(t):
    n = int(input())
    graph = [int(input()) for _ in range(n)]

    visited = [0 for _ in range(n)]
    
    dfs(0, 0)

    print(visited[n-1])
