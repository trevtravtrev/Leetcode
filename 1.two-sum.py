#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        # BRUTE FORCE SOLUTION O(n^2)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

        # BETTER SOLUTION
        hash_map = {}
        for i in range(len(nums)):
            hash_map[nums[i]] = i

        for i in range(len(nums)):
            search_value = target-nums[i]
            if search_value in hash_map and hash_map[search_value] != i:
                return [i, hash_map[search_value]]
        """
        # BEST SOLUTION
        hash_map = {}
        for i in range(len(nums)):
            search_value = target-nums[i]
            if search_value in hash_map:
                return[hash_map[search_value], i]
            hash_map[nums[i]] = i
# @lc code=end

