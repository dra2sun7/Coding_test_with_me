def solution(lines):
    lines.sort()
    cnt = 0
    x = lines[0]
    for i in range(1, len(lines)):
        y = lines[i]
        
        a = max(x[0], y[0])
        b = min(x[1], y[1])
        
        if a < b:
            cnt += b-a
            x = [b, max(x[1], y[1])]
        else:
            x = y
            
    return cnt
        