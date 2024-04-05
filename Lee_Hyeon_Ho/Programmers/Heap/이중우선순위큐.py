import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    cnt = 0
    for x in operations:
        a, b = x.split()
        b = int(b)
        if a == 'I':
            heapq.heappush(min_heap, b)
            heapq.heappush(max_heap, -b)
            cnt += 1
            # max_heap *= 1
            # print(f"insert {b}")
            # print(f"max heap = {max_heap}, min heap = {min_heap}")
            # max_heap *= 1
        else:
            if cnt != 0:
                cnt -= 1
                if b == 1:
                    if len(max_heap) != 0:
                        heapq.heappop(max_heap)
                        # max_heap *= 1
                        # print(f"pop {k * -1}")
                        # print(f"max heap = {max_heap}, min heap = {min_heap}")
                        # max_heap *= 1
                else:
                    if len(min_heap) != 0:
                        heapq.heappop(min_heap)
                        # max_heap *= 1
                        # print(f"pop {k * -1}")
                        # print(f"max heap = {max_heap}, min heap = {min_heap}")
                        # max_heap *= 1
    if cnt == 0:
        return [0, 0]
    else:
        if cnt == 1:
            while True:
                num = heapq.heappop(max_heap) * -1
                if num in min_heap:
                    return [num, num]
        else:
            x = None; y = None
            while x == None or y == None:
                if x == None:
                    num = heapq.heappop(min_heap) * -1
                    if num in max_heap:
                        x = num * -1
                if y == None:
                    num = heapq.heappop(max_heap) * -1
                    if num in min_heap:
                        y = num
            return [y, x]
