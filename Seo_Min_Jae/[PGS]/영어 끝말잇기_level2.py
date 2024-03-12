def loser(i, n):
    return [(i%n)+1, (i//n)+1]

def solution(n, words):
    for i in range(1, len(words)):
        if words[i] in words[:i]:
            return loser(i, n)
        elif words[i][0] != words[i-1][-1]:
            return loser(i, n)
        elif len(words[i]) == 1:
            return loser(i, n)
            
    return [0, 0]