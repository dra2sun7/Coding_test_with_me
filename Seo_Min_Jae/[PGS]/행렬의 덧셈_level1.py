def solution(arr1, arr2):
    answer = []
    res = []
    x = len(arr1)
    y = len(arr1[0])
    for i in range(x):
        for j in range(y):
            res.append(arr1[i][j]+arr2[i][j])
        answer.append(res)
        res = []
    return answer

# 다른 풀이
def solution(arr1, arr2):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(arr1,arr2)]
    return answer