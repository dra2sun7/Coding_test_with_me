def dfs(number, k):
    global answer
    global visited

    p = "".join(number)

    if k == 0:
        if int(p) > int(answer):
            answer = p
        if (p, k) not in visited:
            visited.add((p, k))

    if (p, k) in visited:
        return
    visited.add((p, k))
    
    for i in range(L-1):
        for j in range(i+1, L):
            # 두 자리를 스왑
            number[i], number[j] = number[j], number[i]
            dfs(number, k-1)  # 재귀 호출
            # 원래 상태로 복원
            number[i], number[j] = number[j], number[i]

N = int(input())

for i in range(1,N+1):
    number, k = input().split(" ")
    k = int(k)
    answer = "-1"
    number = list(number)
    visited = set()
    L = len(number)
    dfs(number, k)
    print(visited)
    
    print("#"+ str(i) + " " + "".join(answer))
