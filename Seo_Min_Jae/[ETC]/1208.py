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
    
    # 리스트 정렬 최적화 개선선
    # for _ in range(n):
    #     graph.sort()
    #     graph[0] += 1
    #     graph[-1] -= 1

    print(f"#{test_case} {max(graph) - min(graph)}")

################################################
## Counter를 사용해 일정 크기의 블록 개수로 체크 ##
################################################

from collections import Counter

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    n = int(input())
    graph = list(map(int, input().split()))

    counter = Counter(graph)
    max_height = max(counter)
    min_height = min(counter)

    for _ in range(n):
        if max_height - min_height <= 1:
            break

        counter[max_height] -= 1
        counter[max_height - 1] += 1
        if counter[max_height] == 0:
            max_height -= 1
        
        counter[min_height] -= 1
        counter[min_height + 1] += 1
        if counter[min_height] == 0:
            min_height += 1
    
    print(f"#{test_case} {max_height - min_height}")