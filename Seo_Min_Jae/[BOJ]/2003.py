n, m = map(int, input().split())
arr = list(map(int, input().split()))

count = 0
left = right = 0


while right <= n:
    res = sum(arr[left:right])

    if res < m:
        right += 1
    elif res > m:
        left += 1
    else:
        count += 1
        left += 1

print(count)