def solution(quiz):
    answer = []
    for q in quiz:
        cal, res = q.split("=")
        if eval(cal) == int(res):
            answer.append("O")
        else:
            answer.append("X")
    return answer