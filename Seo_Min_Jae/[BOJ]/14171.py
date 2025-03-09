import sys

N = int(input())
dict = {}
count = 0

for _ in range(N):
    city, state = sys.stdin.readline().split()
    city = city[:2]

    if city == state:
        continue

    if (state, city) not in dict:
        dict[(state, city)] = 0
    
    dict[(state, city)] += 1

    if (city, state) in dict:
        count += dict[(city, state)]

print(count)