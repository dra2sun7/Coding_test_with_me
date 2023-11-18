def solution(n):
    answer = 0
    n = list(str(n))
    for i in n:
        answer += int(i)
    return answer

# 다른 풀이
def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer

def solution(n):
    return sum(int(i) for i in str(n))

def solution(n):
    answer = 0
    while n:
        answer += n%10
        n //= 10
    return answer