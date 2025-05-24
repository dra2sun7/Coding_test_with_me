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

###########################################
##### 아래에서부터 확인하는 방법으로 개선 ######
###########################################

def ladder(x, y):
    visited = [[False]*100 for _ in range(100)]

    while x > 0:
        visited[x][y] = True

        # 왼쪽
        if y > 0 and graph[x][y-1] == 1 and not visited[x][y-1]:
            while y > 0 and graph[x][y-1] == 1:
                y -= 1
                visited[x][y] = True
        # 오른쪽
        elif y < 99 and graph[x][y+1] and not visited[x][y+1]:
            while y < 99 and graph[x][y+1] == 1:
                y += 1
                visited[x][y] = True

        x -= 1

    return y

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    t = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if graph[99][i] == 2:
            res = ladder(99, i)
    
    print(f"#{t} {res}")