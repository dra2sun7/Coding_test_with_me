def solution(friends, gifts):
    
    present = []
    point = []
    number = []
    n = len(friends)
    
    for _ in range(n):
        arr = []
        for _ in range(n):
            arr.append(0)
        present.append(arr)
        point.append(0)
        number.append(0)
    
    for x in gifts:
        arr = x.split(" ")
        present[friends.index(arr[0])][friends.index(arr[1])] += 1
    
    for i in range(n):
        for j in range(n):
            if i != j:
                point[i] += present[i][j]
                point[j] -= present[i][j]
    
    print(point)
    
    for i in range(n):
        for j in range(i+1,n):
            if present[i][j] > present[j][i]:
                number[i] += 1
            elif present[i][j] < present[j][i]:
                number[j] += 1
            else:
                if point[i] > point[j]:
                    number[i] += 1
                elif point[j] > point[i]:
                    number[j] += 1
        # print("friends : " + friends[i] + "     받을 선물 수 :" + str(number[i]))
    
    return max(number)
