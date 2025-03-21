from collections import defaultdict
import heapq
import sys

INF = int(1e9)

def dijkstra(start):
    q = [(0, start)]
    visited[start] = True
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
            
        for v, w in graph[now]:
            if not visited[v]:
                cost = dist + w
                if cost < distance[v]:
                    visited[v] = True
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))

n, m, k, x = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))

visited = [False] * (n+1)
distance = [INF] * (n+1)

dijkstra(x)

if k in distance:
    for i, v in enumerate(distance):
        if v == k:
            print(i)
else:
    print(-1)