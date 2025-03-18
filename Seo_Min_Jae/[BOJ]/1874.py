n = int(input())
stack = []
answer = ''
x = 1

for _ in range(n):
    i = int(input())

    while x <= i:
        stack.append(x)
        answer += '+'
        x += 1
    
    if stack[-1] == i:
        stack.pop()
        answer += '-'
    else:
        answer = "NO"
        break


if answer == "NO":
    print(answer)
else:
    for w in answer:
        print(w)