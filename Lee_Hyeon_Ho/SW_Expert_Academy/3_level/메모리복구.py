def memory(k):
    cnt = 0
    
    for i in range(L):
        if num == k:
            return cnt
        elif k[i] != num[i]:
            cnt += 1
            for j in range(i, L):
                k[j] = abs(k[j] - 1)
    return cnt
    

N = int(input())

for i in range(1, N+1):
    num = list(map(int ,list(input())))
    L = len(num)
    k = []
    for j in range(L):
        k.append(0)
    answer = memory(k)
    
    print(f"#{i} {answer}")