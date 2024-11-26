def cal(string):
    if string < 'N':
        return ord(string) - ord('A')
    else:
        return ord('Z') - ord(string) + 1
    

def dfs(arr, idx, cnt, name):
    global answer
    
    if ''.join(arr) == name:
        if answer == -1:
            answer = cnt
        elif answer > cnt:
            answer = cnt
        return
    
    # 오른쪽으로 이동하면서 다른 문자의 위치(idx)를 확인
    tmp = idx + 1
    while (arr[tmp % N] == name[tmp % N]):
        tmp += 1
    new_idx = tmp%N
    
    # 이동한 만큼 cnt 횟수에 더하기 위한 k 값 생성
    k = (tmp-idx)
    k += cal(name[new_idx])
    
    # 배열에서 해당 idx의 값을 원래 값으로 변경
    temp = arr[new_idx]
    arr[new_idx] = name[new_idx]
    
    # 재귀
    dfs(arr, new_idx, cnt+k, name)
    arr[new_idx] = temp
    
    # 왼쪽으로 이동하면서 다른 문자의 위치(idx)를 확인
    tmp = idx - 1
    while (arr[(tmp + N) % N] == name[(tmp + N) % N]):
        # print(f"앞 문자 : {arr[(tmp+N)%N]} 뒷 문자 : {name[(tmp+N)%N]}")
        tmp -= 1
    
    new_idx = (tmp+N)%N
    
    k = (tmp - idx) * -1
    k += cal(name[new_idx])
    
    temp = arr[new_idx]
    arr[new_idx] = name[new_idx]
    
    dfs(arr, (tmp+N)%N, cnt+k, name)
    arr[new_idx] = temp
    

def solution(name):
    global answer, N

    N = len(name)
    answer = -1
    cnt = 0
    arr = ['A' for _ in range(N)]
    if arr[0] != name[0]:
        cnt += cal(name[0])
        arr[0] = name[0]

    dfs(arr, 0, cnt, name)
    
    return answer