def backtrack(index, path):
    if len(path) == m:
        for x in sorted(path):
            print(x, end=' ')
        print()
        return 
    
    for i in range(index, n+1):
        if i not in path:
            path.append(i)
            backtrack(i+1, path)
            path.pop()

n, m = map(int, input().split())
backtrack(1, [])