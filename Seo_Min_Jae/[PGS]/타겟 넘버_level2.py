def solution(numbers, target):
    answer = 0
    
    def dfs(sum, i):
        nonlocal answer
        if i == len(numbers):
            if sum == target:
                answer += 1
            return
        
        dfs(sum + numbers[i], i+1)
        dfs(sum - numbers[i], i+1)
    
    dfs(0, 0)
    
    return answer