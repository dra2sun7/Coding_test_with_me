def solution(answers):
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    arr = [0, 0, 0]
    for i, x in enumerate(answers, start=1):
        if arr1[(i%5)-1] == x:
            arr[0] += 1
        if arr2[(i%8)-1] == x:
            arr[1] += 1
        if arr3[(i%10)-1] == x:
            arr[2] += 1
    answer = []
    max_num = max(arr)
    for i, x in enumerate(arr, start=1):
        if max_num == x:
            answer.append(i)
    return answer
