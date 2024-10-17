n = int(input())

for i in range(n):
    s = input()
    answer = ''

    q = list(s.split())
    
    while q:
        answer += ' '
        answer += q.pop()
    
    print('Case #{0}:{1}'.format(i+1, answer))