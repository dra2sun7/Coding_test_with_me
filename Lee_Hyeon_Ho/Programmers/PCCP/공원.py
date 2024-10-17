def check_size(park, pos_x, pos_y):
    
    if park[pos_x][pos_y] != "-1":
        return 0
    
    x = len(park)
    y = len(park[0])
    cnt = 1
    while ((pos_x + cnt) < x) and ((pos_y + cnt) < y):
        for i in range(cnt+1):
            if park[pos_x + cnt][pos_y + i] != "-1":
                return cnt
        for i in range(cnt):
            if park[pos_x + i][pos_y + cnt] != "-1":
                return cnt
        cnt += 1

    return cnt

def solution(mats, park):
    answer = 0
    
    x = len(park)
    y = len(park[0])
    
    for i in range(x):
        for j in range(y):
            temp = check_size(park,i,j)
            if temp > answer:
                answer = temp
    if answer == 0:
        return -1
    
    while len(mats):
        if answer >= max(mats):
            return max(mats)
        else:
            mats.remove(max(mats))
            
    if len(mats) == 0:
        return -1
    
    return max(mats)
