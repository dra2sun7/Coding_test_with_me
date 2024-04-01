import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return 0
    while len(scoville) > 1:
        x = heapq.heappop(scoville)
        y = heapq.heappop(scoville)
        heapq.heappush(scoville, x + y * 2)
        answer += 1
        if scoville[0] >= K:
            return answer
    if scoville[0] >= K:
        return answer
    return -1
