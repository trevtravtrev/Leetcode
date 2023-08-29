#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
# length of set will be equal to length of list if all values are unique
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not (len(set(nums)) == len(nums))
        
# @lc code=end

