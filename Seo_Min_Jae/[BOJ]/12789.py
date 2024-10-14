N = int(input())
line = list(map(int, input().split()))

stack = []
res = True

for i in range(1, N+1):
    if i in line:
        while i != line[0]:
            stack.append(line.pop(0))
        line.pop(0)
        continue
    elif i == stack[-1] and len(stack):
        stack.pop()
    else:
        res = False
        break

if res:
    print("Nice")
else:
    print("Sad")  
