x = int(input())
 
for i in range(x):
    print(f"#{i+1} {sum(filter(lambda x: x%2 == 1, map(int, input().split())))}")
