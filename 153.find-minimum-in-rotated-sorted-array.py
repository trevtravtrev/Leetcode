#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        left, right = 0, len(nums)-1
        # edge case if already sorted
        if nums[left] < nums[right]:
            return nums[left]
        while left <= right:
            if nums[left] < nums[right]:
                minimum = min(minimum, nums[left])
                break
            mid = (left + right)//2
            minimum = min(minimum, nums[mid])
            # check if mid point is in left sorted array
            if nums[mid] >= nums[left]:
                left = mid + 1
            # mid is in right sorted array
            else:
                right = mid - 1
        return minimum





# @lc code=end

