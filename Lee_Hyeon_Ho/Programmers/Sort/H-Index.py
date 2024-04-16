import heapq

def solution(citations):
    answer = 0
    heapq.heapify(citations)
    while citations:
        while citations[0] < answer:
            heapq.heappop(citations)
            if len(citations) == 0:
                break
        if answer <= len(citations):
            answer += 1
        else:
            break
    return answer - 1
