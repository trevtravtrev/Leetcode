#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = ""
        for char in s:
            # char.isalnum() is better, check alpha or numeric in 1 line
            if char.isdigit() or char.isalpha():
                alphanumeric+=char
        # string immutable so set variable name to output of lower function
        alphanumeric = alphanumeric.lower()
        # [::-1] reverses a string, copies the string starting at the end, iterating backwards -1 index each time
        if alphanumeric == alphanumeric[::-1]:
            return True
        else:
            return False

        
# @lc code=end

