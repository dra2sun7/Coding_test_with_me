def cal(cnt, x):
    if x == 'E':
        return (1 + cnt * 1)
    elif x == 'I':
        return (1 + cnt * 2)
    elif x == 'O':
        return (1 + cnt * 3)
    else:
        return (1 + cnt * 4)

def solution(word):
    answer = 0
    cnt = 781
    for i,x  in enumerate(word):
        if x == 'A':
            answer += 1
        else:
            answer += cal(cnt, x)
        cnt = (cnt - 1) // 5
    return answer


    # E일때
    # idx == 5 -> 2
    # idx == 4 -> 7
    # idx == 3 -> 32
    # idx == 2 -> 157
    # idx == 1 -> 782
    # I일때
    # idx == 5 -> 3
    # idx == 4 -> 13
    # idx == 3 -> 63
    # idx == 2 -> 313
    # idx == 1 -> 1563
    # O일때
    # idx == 5 -> 4
    # idx == 4 -> 19
    # idx == 3 -> 94
    # idx == 2 -> 469
    # idx == 1 -> 2344
    # U일때
    # idx == 5 -> 5
    # idx == 4 -> 25
    # idx == 3 -> 125
    # idx == 2 -> 625
    # idx == 1 -> 3125
