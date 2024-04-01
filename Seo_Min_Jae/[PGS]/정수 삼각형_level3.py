def solution(triangle):
    answer = 0
    dp = [[] for _ in range(len(triangle))]
    
    dp[0] = triangle[0]
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i].append(triangle[i][j] + dp[i-1][j])
            elif j == len(triangle[i])-1:
                dp[i].append(triangle[i][j] + dp[i-1][j-1])
            else:
                dp[i].append(max(triangle[i][j] + dp[i-1][j-1], triangle[i][j] + dp[i-1][j]))
        answer = max(dp[i])
        
    return answer