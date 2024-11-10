for k in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    L = len(arr)
    answer = 0

    while (N != 0):
        if (arr[-1] - arr[0]) <= 1:
            answer = arr[-1] - arr[0]
            break
        
        arr[0] += 1
        arr[-1] -= 1
        
        # arr[0]을 올리고 arr[-1]을 내리는 후 재정렬
        i = 0
        while (arr[i] > arr[i+1] and i+1 < L):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
        
        # arr[-1]을 내린 후 재정렬
        i = -1
        while (arr[i] < arr[i-1] and i-1 >= -L):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            

        N -= 1
    
    if N == 0:
        answer = arr[-1] - arr[0]
    print(f"arr[0] : {arr[0]}, arr[1] : {arr[1]}, arr[-1] : {arr[-1]}, arr[-2] : {arr[-2]}")
    print(f"#{k} {answer}")
