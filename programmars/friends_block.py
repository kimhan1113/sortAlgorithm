

def solution(m, n, board):
    for r in range(m):
        board[r] = list(board[r])

    answer = 0

    while True:
        blocks = remove_blocks(board, m, n)
        if blocks == 0:
            return answer
        answer += blocks

        # 여기가 잘 이해가 안감 ! (여기가 위에 있는 블록이 내려가는 코드)
        for c in range(n):
            cnt_blank = 0
            for r in range(m-1, -1, -1):
                if board[r][c] == '':
                    cnt_blank += 1
                elif cnt_blank > 0:
                    board[r+cnt_blank][c] = board[r][c]
                    board[r][c] = ''


def remove_blocks(board, m, n) -> int:
    check = [[False for c in range(n)] for r in range(m)]
    for r in range(m-1):
        for c in range(n-1):
            block = board[r][c]
            if block == '':
                continue
            elif board[r+1][c] == block and board[r][c+1] == block and board[r+1][c+1] == block:
                check[r][c] = True
                check[r+1][c] = True
                check[r][c+1] = True
                check[r+1][c+1] = True

    cnt_removed = 0
    for r in range(m):
        for c in range(n):
            if check[r][c]:
                board[r][c] = ''
                cnt_removed += 1

    return cnt_removed


m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
answer = solution(m, n, board)
print(answer)
