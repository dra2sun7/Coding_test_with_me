def solution(dots):
    for i in range(1,4):
        arr1 = dots.copy()
        arr2 = []
        arr2.append(dots[0]); arr2.append(dots[i])
        arr1.pop(i); arr1.pop(0)
        
        if ((arr1[0][0] - arr1[1][0]) / (arr1[0][1] - arr1[1][1]) ==
            (arr2[0][0] - arr2[1][0]) / (arr2[0][1] - arr2[1][1])):
                return 1
    return 0