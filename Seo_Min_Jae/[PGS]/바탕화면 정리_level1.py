def solution(wallpaper):
    location = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                location.append([i, j])
    min_x = len(wallpaper)+1
    min_y = len(wallpaper[0])+1
    max_x = 0
    max_y = 0
    for x, y in location:
        if min_x > x:
            min_x = x
        if min_y > y:
            min_y = y
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    return [min_x, min_y, max_x+1, max_y+1]

# 다른 풀이
def solution(wallpaper):
    a, b = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a)+1, max(b)+1]