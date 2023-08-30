#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        # keys: use a set to create unique keys
        # value: count each key's frequency
        for i in range(len(nums)):
            hash_map.setdefault(nums[i], 0)
            if nums[i] in hash_map:
                hash_map[nums[i]] += 1
        # sorted returns list of key:value tuples for dict items
        # key is a lambda function that sorts by value (the 2nd item in pair)
        # reverse to do largest->smallest order for frequency
        sorted_map = sorted(hash_map.items(), key=lambda item: item[1], reverse=True)
        # returning list of top frequent numbers (dict key) by slicing sorted_map to just 0 to k keys we're looking for
        return [item[0] for item in sorted_map[:k]]
# @lc code=end

