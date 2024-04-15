from collections import deque

def input_node(arr, k):
    if k[0] in arr and k[1] in arr:
        return
    elif k[0] in arr:
        arr.append(k[1])
    else:
        arr.append(k[0])

def fun_1(wires, k):
    wires = deque(wires)
    arr1 = [k[0]]
    arr2 = [k[1]]
    while wires:
        if wires[0][0] in arr1 or wires[0][1] in arr1:
            input_node(arr1, wires[0])
            wires.popleft()
        elif wires[0][0] in arr2 or wires[0][1] in arr2:
            input_node(arr2, wires[0])
            wires.popleft()
        else:
            wires.append(wires.popleft())
            
    return abs(len(arr1) - len(arr2))


def solution(n, wires):
    wires.sort()
    answer = n
    for i in range(n-1):
        arr = wires[:i] + wires[i+1:]
        arr1 = wires[i][0]
        arr2 = wires[i][1]
        k = fun_1(arr, wires[i])
        if answer > k:
            answer = k
    return answer
