import heapq

def solution(jobs):
    answer = 0
    heap = []
    time = 0
    jobs.sort()
    idx = 0
    try:
        while len(jobs) > idx:
            while jobs[idx][0] <= time:
                answer += time - jobs[idx][0]
                heapq.heappush(heap, jobs[idx][1])
                idx += 1
            if len(heap) == 0:
                time += 1
            else:
                work = heapq.heappop(heap)
                time += work
                answer += (len(heap) + 1) * work
    except:
        while len(heap) > 0:
            work = heapq.heappop(heap)
            answer += (len(heap) + 1) * work
    return answer // len(jobs)
