def dfs(index, visited, cnt):
    if visited[index] == True:
        count.append(cnt)
        return
    
    if visited[index] == False:
        visited[index] = True
        cnt += 1
        dfs(graph[index]-1, visited, cnt)


n = int(input())
graph = [int(input()) for _ in range(n)]

count = []


for i in range(n):
    visited = [False for _ in range(n)]
    dfs(i, visited, 0)

print(count.index(max(count))+1)