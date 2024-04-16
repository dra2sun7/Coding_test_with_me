def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    except_token = set()
    for x in reserve:
        if x in lost:
            except_token.add(x)
    for x in except_token:
        lost.remove(x)
        reserve.remove(x)
    for x in reserve:
        if x-1 in lost:
            lost.remove(x-1)
        elif x+1 in lost:
            lost.remove(x+1)
        if len(lost) == 0:
            return n
    return n - len(lost)
