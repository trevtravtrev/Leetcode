#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_substring = []
        longest = 0
        # edge cases
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        for letter in s:
            # duplicate found
            if letter in current_substring:
                # slide window to new substring starting after first duplicate
                current_substring = current_substring[current_substring.index(letter)+1:]
            current_substring.append(letter)
            longest = max(longest, len(current_substring))
        return longest
        
# @lc code=end

