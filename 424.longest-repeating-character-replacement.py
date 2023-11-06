#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        # move head of window forward
        for right in range(len(s)):
            # add 1 to count for that character
            count.setdefault(s[right], 0)
            count[s[right]]+=1
            # if there are more character changes than we're allowed in this window
            # need to move tail of window forward
            # right - left + 1 = window length
            while (right - left + 1) - max(count.values()) > k:
                # remove left character from count and move forward
                count[s[left]]-=1
                left+=1
            result = max(result, (right - left + 1))
        return result
# @lc code=end

