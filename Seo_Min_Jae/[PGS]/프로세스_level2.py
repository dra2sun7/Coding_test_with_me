from collections import deque

def solution(priorities, location):
    answer = 0
    q1 = deque(priorities)
    q2 = deque([i for i in range(0, len(priorities))])
    
    while True:
        if q1[0] == max(q1):
            if q2[0] == location:
                answer += 1
                break
            q1.popleft()
            q2.popleft()
            answer += 1
        else:
            q1.append(q1.popleft())
            q2.append(q2.popleft())
    
    return answer

def solution_ex(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]

    while True:
        cur = queue.pop()
        if any(cur[1]<q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
