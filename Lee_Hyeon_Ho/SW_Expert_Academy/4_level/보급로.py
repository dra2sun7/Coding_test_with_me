def road(x, y, result):
    

T = int(input())

for i in range(1, T+1):
    
    N = int(input())
    arr = []
    
    for _ in range(N):
        tmp = list(map(int, list(input())))
        arr.append(tmp)
    
    result = [[-1 for _ in range(N)] for _ in range(N)]
    
    result[0][0] = arr[0][0]
    
    road(0, 0, result)
        
        