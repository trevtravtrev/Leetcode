#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        ANSWER 1:
        hash_map = {}
        for word in strs:
            # count letters in word
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')] += 1
            # insert into lookup hash map: key = letter count, value = word
            # dict key can't be a list
            key = tuple(count)
            if key in hash_map:
                hash_map[key].append(word)
            else:
                hash_map[key] = [word]
        return list(hash_map.values())
        """
        hash_map = {}
        for word in strs:
            # use sorted word as key for dict
            # sorted() returns sorted list of letters, join them back to one word
            sorted_word = "".join(sorted(word))
            # setdefault sets default list value for key if no value, then append word to values list
            hash_map.setdefault(sorted_word, []).append(word)
        return hash_map.values()

# @lc code=end

