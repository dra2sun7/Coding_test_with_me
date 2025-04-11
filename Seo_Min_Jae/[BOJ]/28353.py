n, k = map(int, input().split())
arr = list(map(int, input().split()))
visited = [False] * n

result = 0

arr.sort(reverse=True)

for i in range(n):
    if k <= arr[i] or visited[i]:
        continue

    target = k - arr[i]
    visited[i] = True

    for j in range(i+1, n):
        if target >= arr[j] and visited[j] == False:
            visited[j] = True
            result += 1
            break

print(result)