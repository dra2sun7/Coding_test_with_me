import heapq

def solution(scoville, K):
    answer = 0    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        
        m1 = heapq.heappop(scoville)
        m2 = heapq.heappop(scoville)
        r = m1 + (m2*2)
        heapq.heappush(scoville, r)
        answer += 1
    
    return answer