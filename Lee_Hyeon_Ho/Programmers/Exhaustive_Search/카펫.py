def find_numbers(num):
    arr = []
    i = 3
    while num//i >= i:
        if num%i == 0:
            arr.append([num//i, i])
        i += 1
    return arr

def solution(brown, yellow):
    arr = find_numbers(brown + yellow)
    
    for x in arr:
        if ((x[0] - 2) * (x[1] - 2)) == yellow:
            return x
    return None
