T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = input()

    password = []

    x = len(arr)//4

    for i in range(x):
        for j in range(0, len(arr), x):
            s = arr[j:j+x]
            if s not in password:
                password.append(s)

        arr = arr[-1] + arr[:len(arr)-1]

    password.sort(reverse=True)
    res = int(password[k-1], 16)
    print(f"#{test_case} {res}")