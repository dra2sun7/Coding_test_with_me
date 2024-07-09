def solution(s):
    cnt = 0
    cnt_zero = 0
    
    while s != '0b1':
        if s[0:2] == '0b':
            s = s[2:]
        cnt_zero += s.count('0')
        s = bin(len(s) - s.count('0'))
        cnt += 1
        
    return [cnt, cnt_zero]

def solution(s):
    cnt = 0
    cnt_zero = 0

    while s != '1':
        cnt_zero += s.count('0')
        s = bin(len(s) - s.count('0'))
        s = s[2:]
        cnt += 1
        
    return [cnt, cnt_zero]