import sys

N, P = map(int, input().split())
stacks = [[] for _ in range(7)]
count = 0

for _ in range(N):
    line, fret = map(int, sys.stdin.readline().split())
    
    while stacks[line] and stacks[line][-1] != fret:
        if fret < stacks[line][-1]:
            stacks[line].pop()
        else:
            stacks[line].append(fret)
        count += 1

    if not stacks[line]:
        stacks[line].append(fret)
        count += 1
    
    print(stacks)
            
print(count)