import sys
n = int(input())
num = list(map(int, input().split()))
answer = []

num.sort()

for i in range(2, num[-1]+1):
    res = 0
    for j in range(n):
        if num[j]%i == 0:
            res += 1
    answer.append(res)

print(max(answer))