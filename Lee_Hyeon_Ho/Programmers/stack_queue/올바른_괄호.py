def solution(s):
    num = 0
    for x in s:
        if x == '(':
            num += 1
        else:
            if num == 0:
                return False
            num -= 1
    if num != 0:
        return False
    return True
