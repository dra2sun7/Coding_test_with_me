from bisect import bisect_left, bisect_right

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

n.sort()

for i in range(M):
    left_index = bisect_left(n, m[i])
    right_index = bisect_right(n, m[i])

    print(right_index - left_index, end=' ')