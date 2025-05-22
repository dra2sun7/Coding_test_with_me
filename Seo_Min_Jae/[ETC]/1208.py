T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    graph = list(map(int, input().split()))

    for _ in range(n):
        max_idx = graph.index(max(graph))
        min_idx = graph.index(min(graph))

        graph[max_idx] -= 1
        graph[min_idx] += 1

    print(f"#{test_case} {max(graph) - min(graph)}")