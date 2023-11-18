def sort(A):
    test = []
    test.insert(0, A[-1])
    for i in range(0, len(A)-1):
        test.insert(i+1, A[i])
    return ''.join(test)

def solution(A, B):
    answer = 0
    for i in range(0, len(A)):
        if A == B:
            break
        else:
            A = sort(A)
            answer += 1
    if answer == len(A):
        answer = -1
    return answer