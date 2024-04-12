def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for i in range(n//2, n+1):
        for j in range(len(citations)):
            if i <= citations[j]:
                if len(citations[j:]) >= i and len(citations[0:j]) <= i:
                    answer = max(answer, i)
    return answer