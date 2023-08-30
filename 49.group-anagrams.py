#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        anagrams = []
        results = []
        for word in strs:
            # count letters in word
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            # insert into lookup hash map: key = index, value = letter count
            hash_map[strs.index(word)] = count
        reversed_hash_map = {}
        for key, value in hash_map.items():
            reversed_hash_map.setdefault(tuple(value), set()).add(strs[key])
        results = [values for key, values in reversed_hash_map.items() if len(values) > 0]
        return results
# @lc code=end

