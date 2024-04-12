from itertools import permutations

def find_decimal(value):
    if value == 1 or value == 0:
        return False
    for i in range(2,value):
        if value%i == 0:
            return False
    return True

def solution(numbers):
    arr = list(map(str, numbers))
    answer = 0
    arr2 = []
    
    for i in range(1,len(arr)+1):
        perms = permutations(numbers, i)
        for perm in perms:
            arr1 = ""
            for element in perm:
                arr1 += element
            arr2.append(int(arr1))
    arr2 = set(arr2)
    print(arr2)
    for x in arr2:
        if find_decimal(x):
            answer += 1
    return answer
