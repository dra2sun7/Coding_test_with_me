def solution(numbers):
    answer = ""
    arr = []
    max_len = 0
    for x in numbers:
        x = str(x)
        arr.append(x)
        if len(x) > max_len:
            max_len = len(x)
    arr.sort(key=lambda x: x * ((max_len // len(x))+ 1),reverse = True)
    
    for x in arr:
        if answer != "0" or x != "0":
            answer += x
    return answer
    
    
    for x in arr:
        if answer != "0" or x != "0":
            answer += x
            # answer에 "000"이 입력되지 않도록 하기 위해서 사용
    return answer
    
    # for x in arr:
    #     answer += x
    # return str(int(answer))
    # 위 코드는 문제에서 제시하는 숫자가 너무 커짐을 막기 위해 str형으로 return 하라는 문장에
    # 위배되는 부분이기 때문에 사용하지 않았다.
