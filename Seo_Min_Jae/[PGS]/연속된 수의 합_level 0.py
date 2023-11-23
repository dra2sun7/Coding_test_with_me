def solution(num, total):
    answer = []
    for i in range(num):
        total -= i
    x = total//num
    for i in range(num):
        answer.append(x+i)
    return answer