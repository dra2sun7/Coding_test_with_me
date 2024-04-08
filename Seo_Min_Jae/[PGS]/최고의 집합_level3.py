def solution(n, s):
    answer = []
    while n:
        if s//n == 0:
            return [-1]
        answer.append(s//n)
        s = s-(s//n)
        n -= 1
    return answer