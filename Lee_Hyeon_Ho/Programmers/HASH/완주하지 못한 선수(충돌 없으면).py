def solution(participant, completion):
    dic = {}
    cnt = 0
    for x in participant:
        dic[hash(x)] = x
        cnt += int(hash(x))
    for x in completion:
        print(dic.pop(hash(x)))
        cnt -= int(hash(x))
    return dic.pop(cnt)