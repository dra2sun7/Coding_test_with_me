def solution(sizes):
    answer = 0
    len1 = 0
    len2 = 0
    for x in sizes:
        x.sort()
        if len2 < x[1]:
            len2 = x[1]
        if len1 < x[0]:
            len1 = x[0]
    return len1 * len2
