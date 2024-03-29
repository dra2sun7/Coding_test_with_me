def solution(priorities, location):
    num = 1
    while len(priorities) != 0:
        if priorities[0] == max(priorities):
            if location == 0:
                break
            priorities.pop(0)
            num += 1
            location -= 1
        else:
            priorities.append(priorities.pop(0))
            if location == 0:
                location = len(priorities) - 1 
            else:
                location -= 1
    return num;
