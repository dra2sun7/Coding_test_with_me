from collections import Counter, deque

def count_dna():
    for key in dict:
        if sub_cnt[key] < dict[key]:
            return False
    
    return True

n, k = map(int, input().split())
arr = list(input())
cnt = list(map(int, input().split()))

dict = {"A": 0, "C":0, "G":0, "T":0}

for i, key in enumerate(dict.keys()):
    dict[key] = cnt[i]

result = 0
window = deque(arr[:k])
sub_cnt = Counter(window)

if count_dna():
    result += 1

for i in range(k, n):
    sub_cnt[window.popleft()] -= 1

    window.append(arr[i])
    sub_cnt[arr[i]] += 1

    if count_dna():
        result += 1

print(result)