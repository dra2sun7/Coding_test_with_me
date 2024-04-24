def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            si, sp = stack.pop()
            answer[si] = i - si
        stack.append((i, p))
    
    while stack:
        i, p = stack.pop()
        answer[i] = len(prices) - i - 1
    
    return answer