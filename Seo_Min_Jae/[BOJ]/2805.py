from bisect import bisect_right

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = 0

start = 1
end = max(arr)

while start <= end:
    total = 0
    mid = (start + end) // 2

    index = bisect_right(arr, mid)

    for i in arr[index:]:
        total += i - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)