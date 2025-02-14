def find_parent(parent, k):
    cnt = 0
    while parent[k] != k:
        k = parent[k]
        cnt += 1
    return k, cnt
    

def solution(n, costs):
    parent = [x for x in range(n)]
    cnt = 0
    tmp = 0
    
    costs.sort(key = lambda x: x[2])
    
    for x, y, cost in costs:
        if tmp == n-1:
            return cnt
        xRoot, xRank = find_parent(parent, x)
        yRoot, yRank = find_parent(parent, y)
        if xRoot == yRoot:
            continue
        elif xRank > yRank:
            tmp += 1
            cnt += cost
            parent[yRoot] = xRoot
        elif xRank < yRank:
            tmp += 1
            cnt += cost
            parent[xRoot] = yRoot
        else:
            tmp += 1
            cnt += cost
            parent[yRoot] = xRoot
        # print(f"parent : {parent}")
        
    return cnt
    