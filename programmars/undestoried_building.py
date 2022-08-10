

def solution(board, skill):
    N, M = len(board), len(board[0])

    check = [[0 for i in range(M)] for j in range(N)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        for r in range(r1, r2+1):
            check[r][c1] += degree
            if c2 + 1 < M:
                check[r][c2+1] -= degree

    answer = 0
    for r in range(N):
        oper = 0
        for c in range(M):
            oper += check[r][c]
            if board[r][c] + oper > 0:
                answer += 1

    return answer


board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2],
         [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]

answer = solution(board, skill)
# print(answer)


def remove_blocks(board, m, n) -> int:
    check = [[False for c in range(n)] for r in range(m)]
    for r in range(m-1):
        for c in range(n-1):
            block = board[r][c]
            if block == "":
                continue
            elif board[r+1][c] == block and board[r+1][c+1] == block and board[r][c+1] == block:
                check[r+1][c] == True
                check[r][c+1] == True
                check[r+1][c+1] == True
                check[r][c] == True

    cnt_removed = 0

    for r in range(m):
        for c in range(n):
            if check[r][c]:
                board[r][c] = ""
                cnt_removed += 1

    return cnt_removed


def solution(m, n, board):

    for r in range(m):
        board[r] = list(board[r])

    answer = 0

    while True:
        blocks = remove_blocks(board, m, n)
        if blocks == 0:
            return answer

        answer += blocks

        for c in range(n):
            cnt_block = 0
            for r in range(m-1,-1, -1):
                if board[r][c] == "":
                    cnt_block += 1
                elif cnt_block > 0:
                    board[r+cnt_block][c] = board[r][c]
                    board[r][c] = ""


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

answer = solution(4, 5, board)
