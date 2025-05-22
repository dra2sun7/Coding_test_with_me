def ladder(start):
    for y in range(100):
        # 왼쪽
        if start > 0 and graph[y][start-1] == 1:
            while 0 < start <= 99 and graph[y][start-1] == 1:
                start -= 1
        # 오른쪽
        elif start < 99 and graph[y][start+1] == 1:
            while 0 <= start < 99 and graph[y][start+1] == 1:
                start += 1

    # 당첨
    print(start)
    if graph[99][start] == 2:
        return True
    
    return False

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if graph[0][i] == 1:
            if ladder(i):
                print(f"#{t} {i}")
                break