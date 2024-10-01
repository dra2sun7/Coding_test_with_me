from collections import deque

N, K = map(int, input().split())
answer = []
q = deque([i for i in range(1, N+1)])

while q:
    for _ in range(K-1):
        q.append(q.popleft())
    answer.append(q.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))