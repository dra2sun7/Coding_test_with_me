def solution(board):
    answer = 0
    n = len(board)
    for x in board:
        x.insert(0, 0)
        x.append(0)
    arr = [0 for i in range(n+2)]
    board.append(arr)
    board.insert(0, arr)
    num = []
    m = len(board)
    print()
    for i in range(1,m-1):
        for j in range(1,m-1):
            if board[i][j] == 1:
                num.append([i, j])
    for x in num:
        for a in range(-1,2):
            for b in range(-1,2):
                board[x[0]+a][x[1]+b] = 1
    board.pop(0)
    board.pop(len(board)-1)
    for x in board:
        x.pop(0)
        x.pop(len(x)-1)
    cnt = 0
    for x in board:
        cnt += x.count(0)
    return cnt