from itertools import permutations

def solution(k, dungeons):
    max_num = 0
    nPr = permutations(dungeons, len(dungeons))
    for perms in nPr:
        num = k
        cnt = 0
        for perm in perms:
            if perm[0] > num:
                break
            else:
                num -= perm[1]
                cnt += 1
        if cnt == len(dungeons):
            return cnt
        elif cnt > max_num:
            max_num = cnt
    return max_num
