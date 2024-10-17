import sys
from collections import deque

graph = []
res = []

for _ in range(3):
    graph.append(list(map(int, input().split())))

q = deque()
for i in range(3):
    q.append((graph[i][0], graph[i][1], graph[i][2]))
    q.append((graph[0][i], graph[1][i], graph[2][i]))

while q:
    a, b, c = q.popleft()

    r = 3
    for k in range(1, 4):
        r = min(r, abs(k-a)+abs(k-b)+abs(k-c))
    res.append(r)

print(min(res))