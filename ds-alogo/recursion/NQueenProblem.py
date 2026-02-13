"""
Problem

N Queen Problem
Given an integer n, find all possible ways to position n queens on an n×n chessboard so that no two queens attack each other.
A queen in chess can move horizontally, vertically, or diagonally.

Do solve the problem using recursion first even if you see some non-recursive approaches.

Example One
{
"n": 4
}

Output:
[
["--q-",
 "q---",
 "---q",
 "-q--"],

["-q--",
 "---q",
 "q---",
 "--q-"]
]
There are two distinct ways four queens can be positioned on a 4×4 chessboard without attacking each other.
The positions may appear in the output in any order. So the same two positions in different
order would be another correct output.

Example Two
{
"n": 2
}
Output:

[
]
No way to position two queens on a 2×2 chessboard without them attacking each other - so empty array.
"""
import copy
directions = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0],
    [1, 1],
    [1, -1],
    [-1, 1],
    [-1, -1]
    ]

def is_valid(board, row, col, n):
    for di in directions:
        i = row + di[0]
        j = col + di[1]
        while 0 <= i < n and 0 <= j < n:
            if board[i][j] == 'q':
                return False
            i = i + di[0]
            j = j + di[1]
    return True

def find_all_arrangements_rec(n, board, row, col, result):
    if 0 <= row < n and 0 <= col < n:
        board[row][col] = 'q'
        isValid =  is_valid(board, row, col, n)
        if isValid:
            if row == n - 1:
                result.append(copy.deepcopy(board.copy()))
                board[row][col] = '-'
                return
            else:
                find_all_arrangements_rec(n, board, row + 1, 0, result)
                board[row][col] = '-'
                find_all_arrangements_rec(n, board, row, col + 1, result)
        else:
            board[row][col] = '-'
            find_all_arrangements_rec(n, board, row, col + 1, result)


def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    result = []
    board = [['-' for _ in range(n)] for _ in range(n)]
    final_str_list = []
    find_all_arrangements_rec(n, board, 0, 0, result)
    line = []
    for res in result:
        line = []
        for row in res:
            line.append("".join(row))
        final_str_list.append(line)

    return final_str_list


"""
Special solution using N-Rook problem
"""

def fina_all_arrangements2(n):

    pos = [i for i in range(0, n)]
    results = []
    final_res_list = []
    fina_all_arrangements2_rec(pos, 0, results)
    for res in results:
        res_list = []
        for row in res:
            str_list = ['-' for _ in range(len(res))]
            str_list[row] = 'q'
            res_list.append("".join(str_list))
        final_res_list.append(res_list)
    return final_res_list

def fina_all_arrangements2_rec(pos, i, result):
    for j in range(0, i - 1):
            if i - 1 - j == abs(pos[i - 1] - pos[j]):
                return
    if i == len(pos):
        result.append(copy.deepcopy(pos.copy()))
    else:
        for j in range(i, len(pos)):
            pos[j], pos[i] = pos[i], pos[j]
            fina_all_arrangements2_rec(pos, i + 1, result)
            pos[j], pos[i] = pos[i], pos[j]

if __name__ == '__main__':
    print(fina_all_arrangements2(12))
    # print(fina_all_arrangements2(12))