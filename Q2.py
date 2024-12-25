def isValidSudoku(board):
    rows = [set() for_in range(9)]
    cols = [set() for_in range(9)]
    boxes = [set() for_in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num = '.':
                continue

            box_index = (r // 3) * 3 + (c // 3)

            if num in rows[r] or num in cols[c] or num in boxes[box_index]:
                return False

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)

            return True
board = [
    ["8","3", ".", ".", "7", ".", ".", ".", "."],
    ["9",".", ".", "1","9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".",".", ".", "6"],
    [".", "6",".", ".", ".", ".", "2", "8","." ],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7","9"]
]

print(isValidSudoku(board))