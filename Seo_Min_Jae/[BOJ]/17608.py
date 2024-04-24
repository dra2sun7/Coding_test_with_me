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

################################################################

import sys
input = sys.stdin.readline

n = int(input())
stack = [int(input()) for _ in range(n)]

stick = stack.pop()
answer = 1

while stack:
    p_stick = stack.pop()
    if stick < p_stick:
        stick = p_stick
        answer += 1

print(answer)