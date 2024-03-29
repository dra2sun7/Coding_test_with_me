def solution(prices):
    answer = []
    prices.pop()
    prices.reverse()
    while prices:
        num = 1
        item = prices.pop()
        for x in reversed(prices):
            if x < item:    
                break
            num += 1
        answer.append(num)
    answer.append(0)
    return answer
