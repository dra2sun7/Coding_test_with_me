n, m = map(int, input().split())
floor = []
answer = 0

for _ in range(n):
    floor.append(input())

visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(i, j, x):
    if i >= n or j >= m:
        return

    if floor[i][j] != x:
        return
    
    visited[i][j] = 1

    if x == '-':
        dfs(i, j+1, '-')
    if x == '|':
        dfs(i+1, j, '|')
    
    

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            dfs(i, j, floor[i][j])
            answer += 1

print(answer)
