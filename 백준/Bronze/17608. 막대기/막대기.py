import sys
input = sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]
answer = 0
max_h = 0

for i in range(n-1, -1, -1):
    if stack[i] > max_h:
        answer += 1
        max_h = stack[i]

print(answer)