from collections import deque

N = int(input())
q = deque()

for _ in range(N):
    initial, num = input().split()
    q.append([initial, num])

while len(q)>1:
    i, n = q.popleft()
    for _ in range(int(n)-1):
        q.append(q.popleft())
    q.popleft()

print(q.popleft()[0])