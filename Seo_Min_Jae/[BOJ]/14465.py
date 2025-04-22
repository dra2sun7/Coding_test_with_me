from collections import deque, Counter

n, k, b = map(int, input().split())
arr = [0] * (n+1)

for _ in range(b):
    arr[int(input())] = 1

window = deque(arr[1:k+1])
count = Counter(window)
res = count[1]

for i in range(k+1, n+1):
    count[window.popleft()] -= 1
    window.append(arr[i])
    count[arr[i]] += 1
    
    res = min(res, count[1])

print(res)