from collections import defaultdict

def solution(keymap, targets):
    answer = []
    cnt = defaultdict()
    
    for s in keymap:
        for i in s:
            if i not in cnt:
                cnt[i] = s.index(i)+1
            cnt[i] = min(cnt[i], s.index(i)+1)

    for t in targets:
        res = 0
        for j in t:
            if j not in cnt:
                res = -1
                break
            res += cnt[j]
        answer.append(res)
    
    return answer