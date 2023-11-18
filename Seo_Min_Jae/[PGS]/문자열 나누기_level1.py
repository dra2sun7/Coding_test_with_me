from collections import deque

def solution(s):
    a, b = deque(), deque()
    answer = 0
    for i in s:
        # a에 값이 존재할 때
        if a:
            # 기준 값과 i가 같다면
            if num == i:
                a.append(i)
            else:
                b.append(i)
        # a에 아무것도 없을 때
        else:
            a.append(i)
            num = i
        # 갯수 비교
        if len(a) == len(b):
            answer+=1
            a.clear()
            b.clear()
    # 마지막 값이 존재할 경우, 나머지가 존재할 경우
    if a:
        answer += 1
    return answer

# level 1을 스스로 풀다니...!! 물론 deque에 대해 찾아보긴 했지만ㅎㅎ
# 큐 더 공부해서 쓰는 법을 찾아봐야지.. 야매(?)로 쓴거라서.. 사실 저렇게 쓸거면 list를 썼어도..

# 다른 풀이
def solution(s):
    answer = 0
    sav1 = 0
    sav2 = 0
    for i in s:
        if sav1 == sav2:
            answer += 1
            a = i
        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    return answer

from collections import deque

def solution(s):
    ans = 0
    q = deque(s)
    while q:
        a, b = 1, 0
        x = q.popleft()

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1
            
            if a == b:
                ans += 1
                break
    if a != b:
        ans += 1
    
    return ans