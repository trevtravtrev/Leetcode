#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n, results, after_self_prod = len(nums), [1]*len(nums), 1
        # calculate before self product
        # start i at "1" since index 0 doesn't have before self values
        for i in range(1, n):
            # each next result is the product of the last result and next number from nums
            results[i] = results[i-1]*nums[i-1]
        # calculate product of before self and after self
        # start at max nums index, go to 0 index (-1 since exclusive), iterate backwards
        for i in range(n-1, -1, -1):
            # product of before self and after self in results
            results[i] *= after_self_prod
            # update after self product for next iteration
            after_self_prod *= nums[i]
        return results



# @lc code=end