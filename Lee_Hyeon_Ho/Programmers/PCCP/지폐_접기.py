def solution(wallet, bill):
    answer = 0
    while max(wallet) < max(bill) or min(wallet) < min(bill):
        if max(bill) ==  bill[0]:
            bill[0] = int(bill[0]/2)
        else:
            bill[1] = int(bill[1]/2)
        answer += 1
        print(bill)
    return answer
