def back(res):
    if len(res) == m:
        print(*res)
        return
    
    for i in range(1, n+1):
        res.append(i)
        back(res)
        res.pop()


n, m = map(int, input().split())
back([])