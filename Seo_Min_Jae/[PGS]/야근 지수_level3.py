import heapq

def solution(n, works):
    answer = 0
    
    if sum(works) < n:
        return 0
    
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
        
    for i in range(n):
        x = heapq.heappop(heap)
        heapq.heappush(heap, -((-x)-1))
    
    for x in heap:
        answer += x**2
    
    return answer