def add(x, y):
    s = 0

    for mi in range(m):
        nx = x + mi
        for mj in range(m):
            ny = y + mj

            s += graph[nx][ny]

    return s

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    k = 0

    for i in range(0, n-m+1):
        for j in range(0, n-m+1):
            res = max(res, add(i, j))

    print(f"#{test_case} {res}")