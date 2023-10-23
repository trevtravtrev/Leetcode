#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # use last in first out stack to check order of brackets
        stack = []
        brackets = {"(": ")", "{": "}", "[": "]"}
        if len(s)%2 != 0:
            return False
        for char in s:
            if char in brackets.keys():
                stack.append(brackets.get(char))
            else:
                if len(stack) == 0:
                    return False
                else:
                    closed_bracket = stack.pop()
                    if char == closed_bracket:
                        continue
                    else:
                        return False
        # edge case for example "((" with no closing brackets
        if len(stack) == 0:
            return True
            
        
# @lc code=end

