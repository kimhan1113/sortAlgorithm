

def solution(triangle):
    n = len(triangle)
    dp = [[0 for j in range(i+1)] for i in range(n)]

    dp[0][0] = triangle[0][0]
    for i in range(n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]

    return max(dp[-1])


dp = [[0 for j in range(i+1)] for i in range(5)]
print(dp)





def solution(triangle):

    n = len(triangle)
    dp = [[0 for j in range(i+1)] for i in range(n)]

    dp[0][0] = triangle[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        dp[i][-1] = dp[i-1][-1] + triangle[i][-1]    

    return max(dp[-1])