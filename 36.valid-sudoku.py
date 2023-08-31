#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create hash map for board coordinates:value
        # key: tuple(coordinates), value: number in square
        board_hash = {}
        numbers = []
        unique_numbers = []
        for row in range(9):
            for column in range(9):
                coordinate = (row, column)
                value = board[row][column]
                board_hash.setdefault(coordinate, value)
        board_items = board_hash.items()
        # verify correct values in row
        for i in range(len(board_items)):
            value = board_hash[i][1]
            if value != ".":
                numbers.append(value)
        unique_numbers = set(numbers)
        if len(unique_numbers) != len (numbers):
            return False
        # verify correct values in column
        # verify correct values in squares

# @lc code=end

