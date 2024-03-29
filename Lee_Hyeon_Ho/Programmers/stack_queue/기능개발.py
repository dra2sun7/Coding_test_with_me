def solution(progresses, speeds):
    answer = [0]
    while len(speeds) != 0:
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            flag = 0
            while progresses[0] >= 100:
                progresses.pop(0); speeds.pop(0);
                answer[-1] += 1
                if len(speeds) == 0:
                    flag = 1
                    break
            if flag != 1:
                answer.append(0)
    return answer
