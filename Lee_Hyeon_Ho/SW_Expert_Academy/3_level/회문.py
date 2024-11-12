def check_list(arr):
    def width(arr):
        cnt = 0
        for x in range(8):
            for y in range(8-N+1):
                L = []
                for k in range(N):
                    L.append(arr[x][y+k])
                if L == list(reversed(L)):
                    cnt += 1
        return cnt


    def height(arr):
        cnt = 0
        for y in range(8):
            for x in range(8-N+1):
                L = []
                for k in range(N):
                    L.append(arr[x+k][y])
                if L == list(reversed(L)):
                    cnt += 1
                    
        return cnt
    
    return width(arr) + height(arr)
            
    

for i in range(1, 11):
    N = int(input())
    arr = []

    for j in range(8):
        tmp = list(input())
        arr.append(tmp)
        
    cnt = check_list(arr)

    print(f"#{i} {cnt}")