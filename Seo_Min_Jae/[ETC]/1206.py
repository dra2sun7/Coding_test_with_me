T = 10

for test_case in range(1, T + 1):

    n = int(input())
    graph = list(map(int, input().split()))

    res = 0

    for i in range(2, n-2):
        lmax = max(graph[i-2:i])
        rmax = max(graph[i+1:i+3])

        if graph[i] > lmax and graph[i] > rmax:
            res += graph[i] - max(lmax, rmax)

    print(f"#{test_case} {res}")