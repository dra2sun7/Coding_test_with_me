def solution(number, k):
    stack = []
    for x in number:
        while stack and k > 0 and stack[-1] < x:
            stack.pop()
            k -= 1
        stack.append(x)
    while k != 0:
        stack.pop()
        k -= 1
    return ''.join(stack)