from bisect import bisect_left

N = int(input())
n = list(map(int, input().split()))
M = int(input())
m = list(map(int, input().split()))

n.sort()

for i in range(M):
    index = bisect_left(n, m[i])

    if index < N and n[index] == m[i]:
        print(1, end=' ')
    else:
        print(0, end=' ')