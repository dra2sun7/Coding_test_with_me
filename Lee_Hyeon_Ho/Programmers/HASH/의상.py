def solution(clothes):
    answer = 1
    dic = {}
    for x in clothes:
        if x[1] not in dic:
            dic[x[1]] = 1
        else:
            dic[x[1]] += 1
    for x in dic:
        answer *= dic[x] + 1
    return answer - 1
