def solution(lottos, win_nums):
    answer = []
    zero = lottos.count(0)
    cnt = 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    answer.append(rank[cnt+zero])
    answer.append(rank[cnt])
    return answer