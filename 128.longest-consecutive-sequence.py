#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # longest length of consecutives
        longest = 1
        # current length of consecutives
        length = 1
        # unique numbers sorted in ascending order
        ordered_unique_nums = sorted(set(nums))
        # amount of unique nums
        n = len(ordered_unique_nums)
        # if no numbers return 0
        if n == 0:
            return 0
        # if 1 number return 1
        elif n == 1:
            return 1
        # iterate over ordered unique nums starting at 2nd number
        for i in range(1, n):
            # if consecutive number (current num equal to previos num + 1)
            if ordered_unique_nums[i] == ordered_unique_nums[i-1]+1:
                # add to current consecutive length
                length += 1
            # if not consecutive
            else:
                # reset current consecutive length
                length = 1
            # if current consecutive length is greater than overall longest
            if length > longest:
                # set longest to current length
                longest = length
        return longest

# @lc code=end

