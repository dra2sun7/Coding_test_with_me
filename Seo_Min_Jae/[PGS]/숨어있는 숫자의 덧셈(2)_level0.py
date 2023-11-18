#1117
def solution(my_string):
    answer = 0
    num=""
    res=[]
    for s in my_string:
        if s.isdigit():
            num+=s
        else:
            if num != "":
                res.append(int(num))
                num=""
    if num != "":
        res.append(int(num))
    answer += sum(res)
    return answer

#이전
def solution(my_string):
    answer = 0
    n = '0'
    for i in my_string:
        if not i.isdigit():
            answer += int(n)
            n = '0'
        else:
            n += i
    answer += int(n)
    return answer

#간단한 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())