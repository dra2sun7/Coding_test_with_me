import heapq

def solution(jobs):
    answer = 0
    real_time = 0
    heapq.heapify(jobs)
    # 최솟값을 뜻하는 문제가 나타나면 대부분 heap을 이용해서 해결
    print(jobs)
    return answer

solution([[0, 3], [0, 2], [0, 1],  [10, 3], [1, 9], [1, 6], [2, 3]])

