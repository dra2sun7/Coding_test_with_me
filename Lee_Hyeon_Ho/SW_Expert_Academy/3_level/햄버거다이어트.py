def hamburger(ingredient, ham, k):
    global calories
    global satisfy
    
    for i in range(k, len(ingredient)):
        if ham[1] + ingredient[i][1] < L:
            ham[0] += ingredient[i][0]
            ham[1] += ingredient[i][1]
            hamburger(ingredient, ham, i+1)
            ham[0] -= ingredient[i][0]
            ham[1] -= ingredient[i][1]
    if ham[0] > satisfy:
        satisfy = ham[0]
    

T = int(input())

for i in range(1, T+1):
    N, L = map(int, input().split())
    ingredient = []
    satisfy = 0
    
    for _ in range(N):
        tmp = list(map(int, input().split()))
        ingredient.append(tmp)
    
    hamburger(ingredient, [0, 0], 0)
    print(f"{i} {satisfy}")