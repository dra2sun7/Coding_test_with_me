def nQueen(chess, x):
    def is_safe(chess, x, y):
        for i in range(x):
            if chess[i][y] == 1:
                return False
            
        i = 1
        while (x - i >= 0 and y - i >= 0):
            if chess[x-i][y-i] == 1:
                return False
            i += 1
            
        i = 1
        while (x - i >= 0 and y + i < N):
            if chess[x-i][y+i] == 1:
                return False
            i += 1
            
        return True
        
    global cnt
    
    if x == N:
        cnt += 1
        return
    
    for y in range(N):
        if is_safe(chess, x, y):
            chess[x][y] = 1
            nQueen(chess, x+1)
            chess[x][y] = 0
        

T = int(input())

for i in range(1, T+1):
    N = int(input())
    cnt = 0
    chess = [[0 for _ in range(N)] for _ in range(N)]
    
    nQueen(chess, 0)
    
    print(f"#{i} {cnt}")