from collections import deque

n = int(input())
queue = deque([i for i in range(1, n+1)])
answer = []

while len(queue) > 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())

answer.append(queue.popleft())

for i in answer:
    print(i, end=' ')
