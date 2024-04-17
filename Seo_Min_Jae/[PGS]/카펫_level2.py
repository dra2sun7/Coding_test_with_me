def solution(brown, yellow):
    answer = []
    y = []
    
    for i in range(1, yellow+1):
        if yellow%i == 0:
            if i >= yellow//i:
                y.append([i, yellow//i])
    
    for l in y:
        if sum(l)*2 == brown-4:
            answer.append(l[0]+2)
            answer.append(l[1]+2)
            break
    
    return answer