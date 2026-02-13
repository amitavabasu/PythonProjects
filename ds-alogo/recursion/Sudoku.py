"""
Problem

Sudoku Solver
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row, each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.

Unfilled cells have a value of 0 on the given board.

Example
Example one

{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}
Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]
Notes
You can assume that any given puzzle will have exactly one solution.

Constraints:

Size of the input array is exactly 9 x 9
0 <= value in the input array <= 9
"""

def is_valid(board, row, col, val):
    if val in board[row]:
        return False
    if val in [ board[i][col] for i in range(9) ]:
        return False

    boxRow = row - (row % 3)
    boxCol = col - (col % 3)
    for i in range(boxRow, boxRow + 3):
        for j in range(boxCol, boxCol + 3):
            if board[i][j] == val:
                return False
    return True


def solve_sudoku_puzzle_rec(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # global row, col
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row, col = i, j
                break
        else:
            continue
        break
    else:
        return True

    for val in range(1, 10):
        if is_valid(board, row, col, val):
            board[row][col] = val
            if solve_sudoku_puzzle_rec(board):
                return True
            else:
                board[row][col] = 0

    return False

def solve_sudoku_puzzle(board):
    print(solve_sudoku_puzzle_rec(board))
    return board

if __name__ == '__main__':
    board =  [
        [8, 4, 9, 0, 0, 3, 5, 7, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0],
        [7, 0, 0, 0, 9, 0, 0, 8, 3],
        [0, 0, 0, 9, 4, 6, 7, 0, 0],
        [0, 8, 0, 0, 5, 0, 0, 4, 0],
        [0, 0, 6, 8, 7, 2, 0, 0, 0],
        [5, 7, 0, 0, 1, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 2, 1, 7, 0, 0, 8, 6, 5]
    ]
    print(board)
    print(solve_sudoku_puzzle(board))





