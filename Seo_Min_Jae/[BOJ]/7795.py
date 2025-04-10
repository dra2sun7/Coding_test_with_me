from bisect import bisect_left

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    res = 0

    for i in a:
        res += bisect_left(b, i)
    
    print(res)