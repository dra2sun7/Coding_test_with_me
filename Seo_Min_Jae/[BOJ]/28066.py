from collections import deque

N, K = map(int, input().split())
q = deque([i for i in range(1, N+1)])

while len(q) > 1:
    q.append(q.popleft())

    if len(q) < K:
        count = len(q)
    else:
        count = K

    for _ in range(count-1):
        q.popleft()

print(q.popleft())