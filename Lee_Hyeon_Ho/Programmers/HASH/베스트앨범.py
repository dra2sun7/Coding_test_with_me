def solution(genres, plays):
    dic1 = {}
    dic2 = {}
    for i,x in enumerate(genres):
        if x not in dic1:
            dic1[x] = plays[i]
        else:  
            dic1[x] += plays[i]
    for x in dic1:
        dic2[x] = []
        num1 = 0; num2 = 0;
        for i,y in enumerate(genres):
            if x == y:
                if len(dic2[x]) == 0:
                    dic2[x].append(i); num1 = plays[i]
                elif len(dic2[x]) == 1:
                    if num1 < plays[i]:
                        num2 = num1; num1 = plays[i];
                        dic2[x].insert(0, i)
                    else:
                        num2 = plays[i]
                        dic2[x].append(i)
                else:
                    if num2 < plays[i]:
                        if num1 < plays[i]:
                            num2 = num1; num1 = plays[i];
                            dic2[x].pop(-1); dic2[x].insert(0, i)
                        else:
                            num2 = plays[i]
                            dic2[x].pop(-1); dic2[x].append(i)
    answer = []
    while len(dic1) != 0:
        num = 0
        a = ''
        for x in dic1:
            if num < dic1[x]:
                num = dic1[x]; a = x;
        dic1.pop(a)
        answer += dic2[a]

    return answer
