def nQueen(n):
    board = [["."]*n for i in range(n)]
    result = []
    cols = set()
    pos_dig = set()
    neg_dig = set()
    print(board)
    def backtrack(row):
        if row == n:
            result.append([" ".join(_) for _ in board])
            return
        for col in range(n):
            if col in cols or (row+col) in pos_dig or (row-col) in neg_dig:
                continue
            
            board[row][col] = "Q"
            cols.add(col)
            pos_dig.add(row+col)
            neg_dig.add(row-col)

            backtrack(row+1)

            board[row][col] = "."
            cols.remove(col)
            pos_dig.remove(row+col)
            neg_dig.remove(row-col)

    backtrack(0)
    return result




solutions = nQueen(4)
for s in solutions:
    for row in s:
        print(row)
    print()