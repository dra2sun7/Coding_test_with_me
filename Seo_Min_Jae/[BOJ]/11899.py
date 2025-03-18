S = input()

stack = []

for s in S:
    if stack and s == ")" and stack[-1] == "(":
        stack.pop()
    else:
        stack.append(s)

print(len(stack))