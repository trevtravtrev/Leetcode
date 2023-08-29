#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagrams must be same length
        if len(s) != len(t):
            return False
        
        s = s.lower()
        t = t.lower()
        s_letters = [0]*26
        t_letters = [0]*26

        for i in range(len(s)):
            # count how many of each letter in each string
            s_letters[ord(s[i])-ord('a')] += 1
            t_letters[ord(t[i])-ord('a')] += 1

        # both strings should have same amount of each letter
        if s_letters == t_letters:
            return True
        else:
            return False


        
# @lc code=end

