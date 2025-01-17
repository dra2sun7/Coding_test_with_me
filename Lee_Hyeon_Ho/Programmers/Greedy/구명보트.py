def solution(people, limit):
    answer = 0
    people.sort()
    fidx = 0
    bidx = len(people) - 1
    while (fidx <= bidx):
        tmp = people[bidx]
        answer += 1
        if (tmp + people[fidx] <= limit and fidx < bidx):
            fidx += 1
        bidx -= 1
    return answer