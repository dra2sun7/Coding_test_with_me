T = 10
for test_case in range(1, T + 1):
    test_case = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    row = col = left_diagnol = right_diagnol = 0
    res = []

    for i in range(100):
        for j in range(100):
            row += graph[i][j]
            col += graph[j][i]
            if i == j:
                left_diagnol += graph[i][j]
            if i + j == 99:
                right_diagnol += graph[i][j]
        res.append(row)
        res.append(col)
        row = col = 0

    res.append(left_diagnol)
    res.append(right_diagnol)
    print(f"#{test_case} {max(res)}")

#########################################
    max_val = 0
    left_diag = 0
    right_diag = 0

    for i in range(100):
        row_sum = sum(graph[i])
        col_sum = sum(graph[i][j] for j in range(100))

        max_val = max(max_val, row_sum, col_sum)

        left_diag += graph[i][i]
        right_diag += graph[i][99-i]

    max_val = max(max_val, left_diag, right_diag)
    print(f"#{test_case} {max_val}")
