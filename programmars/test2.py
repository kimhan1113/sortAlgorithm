





def solution(diet):

    dp = [[0 for _ in range(3)] for _ in range(len(diet))]
    dp[0] = diet[0]

    for i in range(1, len(diet)):
        for j in range(3):

            if j == 0:               
                dp[i][j] = min(diet[i][j]+ dp[i-1][j], diet[i][j]+ dp[i-1][j+1], diet[i][j]+ dp[i-1][j+2])

            elif j == 1:     
                dp[i][j] = min(diet[i+1][j]+ dp[i-1][j], diet[i][j]+ dp[i-1][j+1])

            else:
                dp[i][j] = min(diet[i+1][j]+ dp[i-1][j], diet[i][j]+ dp[i-1][j+1])    

    answer = 0
    return answer

# answer = solution(diet)
# print(answer)
diet = [[360,138,338], [230,102,311], [320,474,214], [131,498,484], [366,176,249], [323,407,116], [265,433,317]]




# print(len(temp))



def solution_(diet):

    temp = []

    for d in diet:
        temp.extend(d)

    dp = [0] * len(temp)

    dp[0] = temp[0]
    dp[1] = temp[1]
    dp[2] = temp[2]

    for i in range(3, len(temp)):

        dp[i] = min(temp[i]+dp[i-3],temp[i]+dp[i-2],temp[i]+dp[i-1])
        
    return min(dp[-3:])
    
answer = solution_(diet)
print(answer)