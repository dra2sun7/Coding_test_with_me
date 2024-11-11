def farming(farm):
    global cnt
    
    x = 0
    for i in range(half + 1):
        for y in range(half - i, N - half + i):
            cnt += int(farm[x][y])
            # farm[x][y] = "*"
        x += 1
    
    for i in range(1,half+1):
        for y in range(i, N - i):
            cnt += int(farm[x][y])
            # farm[x][y] = "*"
        x += 1

T = int(input())

for i in range(1,T+1):
    cnt = 0
    farm = []
    N = int(input())
    half = int(N/2)
    for j in range(N):
        tmp = list(input())
        farm.append(tmp)
    
    farming(farm)
    
    # for j in range(N):
    #     print(farm[j])
        
    # print("==============================")
    
    print(f"#{i} {cnt}")