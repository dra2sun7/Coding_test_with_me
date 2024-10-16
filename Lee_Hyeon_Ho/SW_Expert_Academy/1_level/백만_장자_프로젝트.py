x = int(input())

for i in range(x):
    num = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    max_num = arr.pop()
    while len(arr) > 0:
        if arr[-1] < max_num:
            cnt += max_num - arr[-1]
        elif arr[-1] > max_num:
            max_num = arr[-1]
        arr.pop()
    print(f"#{i+1} {cnt}")
