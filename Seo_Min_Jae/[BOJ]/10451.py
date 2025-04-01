from collections import defaultdict

t = int(input())

def dfs(node):
    if visited[node] == True:
        return False
    
    visited[node] = True

    if visited[graph[node]] == False:
        dfs(graph[node])
    
    return True

for _ in range(t):
    n = int(input())
    graph = [0]
    nums = list(map(int, input().split()))
    for num in nums:
        graph.append(num)

    visited = [False] * (n+1)
    count = 0

    for i in range(1, n+1):
        if dfs(i):
            count += 1
    
    print(count)