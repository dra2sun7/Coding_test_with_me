T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))

    res = 0
    max_price = 0

    for i in range(n-1, -1, -1):
        max_price = max(max_price, prices[i])

        if max_price > prices[i]:
            res += max_price - prices[i]

    print(f'#{test_case} {res}')