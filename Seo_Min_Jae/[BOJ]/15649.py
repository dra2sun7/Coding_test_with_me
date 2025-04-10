def backtrack(path):
    if len(path) == m:
        for x in path:
            print(x, end=' ')
        print()
        return 
    
    for i in range(1, n+1):
        if i not in path:
            path.append(i)
            backtrack(path)
            path.pop()


n, m = map(int, input().split())
backtrack([])