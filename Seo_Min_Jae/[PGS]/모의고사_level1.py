def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a_cnt = 0
    b_cnt = 0
    c_cnt = 0
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            a_cnt += 1
        if answers[i] == b[i%len(b)]:
            b_cnt += 1
        if answers[i] == c[i%len(c)]:
            c_cnt += 1
    max_cnt = max(a_cnt, b_cnt, c_cnt)
    if max_cnt == a_cnt:
        answer.append(1)
    if max_cnt == b_cnt:
        answer.append(2)
    if max_cnt == c_cnt:
        answer.append(3)
    return answer

# 더 깔끔한 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result