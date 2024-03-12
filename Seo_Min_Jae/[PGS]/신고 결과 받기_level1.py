import collections

def solution(id_list, report, k):
    answer = []
    del_dict = collections.defaultdict(list)
    total = collections.defaultdict(int)
    
    # 신고 dict
    for r in set(report):
        u1, u2 = r.split(' ')
        del_dict[u2].append(u1)
    
    
    # k번 이상 신고 받은 user를 신고한 user가 받을 이메일 갯수
    for u, v in del_dict.items():
        if len(v) >= k:
            for id in v:
                total[id] += 1
    
    # id_list에 따라 total에서 찾아 answer 정리
    for id in id_list:
        if id in total:
            answer.append(total[id])
        else:
            answer.append(0)
    
    return answer