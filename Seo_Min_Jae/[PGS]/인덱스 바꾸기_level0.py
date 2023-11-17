def solution(my_string, num1, num2):
    answer = ''
    for i in range(0, len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer

# 다른 풀이
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)
# list로 바꿔줘야 15번째 줄처럼 값 바꾸기가 가능