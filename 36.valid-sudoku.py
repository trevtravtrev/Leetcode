#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9 sets of row values
        rows = [set() for x in range(9)]
        # 9 sets of column values
        columns = [set() for x in range(9)]
        # 3 lists of 3 sets, will use // to know which square
        squares = [[set() for x in range(3)] for y in range(3)]

        # ADD VALUES TO ROWS, COLUMNS, SQUARES LISTS
        # iterate over lists that contain row values
        for i in range(9):
            # iterate over values
            for j in range(9):
                value = board[i][j]
                if value.isdigit():
                    if value in rows[i] or value in columns[j] or value in squares[i//3][j//3]:
                        return False
                    # add row values
                    rows[i].add(value)
                    # add column values
                    columns[j].add(value)
                    # add square values
                    """
                    Indexes range from 0 to 8.
                    0 // 3 = 0
                    1 // 3 = 0
                    2 // 3 = 0
                    3 // 3 = 1
                    4 // 3 = 1
                    5 // 3 = 1
                    6 // 3 = 2
                    7 // 3 = 2
                    8 // 3 = 2
                    """
                    squares[i//3][j//3].add(value)
        return True

# @lc code=end

