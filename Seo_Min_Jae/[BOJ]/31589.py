n, k = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = []

left = 0
right = n-1

while k > 0:
    result.append(arr[right])
    right -= 1
    k -= 1

    if k > 0:
        result.append(arr[left])
        left += 1
        k -= 1

answer = 0

for i in range(len(result)):
    if i == 0:
        answer += result[i]
    elif result[i-1] < result[i]:
        answer += result[i] - result[i-1]

print(answer)