T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    res = 0

    for i in range(0, n//2):
        res += sum(graph[i][n//2-i:n//2+i+1])

    for j in range(n//2, n):
        res += sum(graph[j][j-n//2:n-(j-n//2)])
    
    # center = n//2

    # for i in range(n):
    #     offset = abs(center - i)
    #     start = offset
    #     end = n - offset
    #     res += sum(graph[i][start:end])

    print(f"#{test_case} {res}")