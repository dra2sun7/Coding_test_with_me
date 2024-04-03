def solution(numbers, hand):
    answer = ''
    keypad = [[1, 4, 7, '*'], [2, 5, 8, 0], [3, 6, 9, '#']]
    location = [[0, 3], [2, 3]]
    
    for n in numbers:
        if n in keypad[0]:
            answer += 'L'
            location[0] = [0, keypad[0].index(n)]
        elif n in keypad[2]:
            answer += 'R'
            location[1] = [2, keypad[2].index(n)]
        else:
            x, y = 1, keypad[1].index(n)
            l = abs(location[0][0] - x) + abs(location[0][1] - y)
            r = abs(location[1][0] - x) + abs(location[1][1] - y)
            if l < r:
                answer += 'L'
                location[0] = [x, y]
            elif l > r:
                answer += 'R'
                location[1] = [x, y]
            else:
                if hand == 'left':
                    answer += 'L'
                    location[0] = [x, y]
                else:
                    answer += 'R'
                    location[1] = [x, y]
    
    return answer