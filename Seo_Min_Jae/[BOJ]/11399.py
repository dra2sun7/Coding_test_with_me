n = int(input())
arr = sorted(map(int, input().split()))

result = 0
prev = 0

for i in arr:
    result += prev + i
    prev += i

print(result)