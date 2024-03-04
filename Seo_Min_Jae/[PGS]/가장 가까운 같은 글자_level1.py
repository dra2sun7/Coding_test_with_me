def solution(s):
    answer = []
    index = {}
    for i in range(len(s)):
        if s[i] not in index:
            index[s[i]] = i
            answer.append(-1)
        else:
            answer.append(i - index[s[i]])
            index[s[i]] = i
    return answer