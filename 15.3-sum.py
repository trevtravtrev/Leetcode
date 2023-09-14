#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        num_zeros = 0

        # separate negatives, positives, and zero
        negatives, positives, zero = [], [], False
        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)
            else:
                zero = True
                # case 2: 3 zeros
                num_zeros+=1

        # convert positive/negative lists to sets just for o(1) lookup times
        # we'll still use original positive/negative lists to index values
        unique_negatives, unique_positives = set(negatives), set(positives)

        # case 1: zero exists, find complements
        if zero:
            for negative in unique_negatives:
                if -1*negative in unique_positives:
                    # sort list values with sorted, sorted returns a list
                    # convert list to tuple so it can be added to set (lists can't since they're unhashable)
                    triplets.add(tuple(sorted([negative, 0, -1*negative])))
        
        # case 2: 3 zeros
        if num_zeros >= 3:
            triplets.add((0, 0, 0))
        
        # case 3: for all combinations of positives, check if negative complement exists
        num_positives = len(positives)
        for i in range(num_positives):
            for j in range(i+1, num_positives):
                target = -1*(positives[i]+positives[j])
                if target in unique_negatives:
                    triplets.add(tuple(sorted([positives[i], positives[j], target])))
        
        # case 4: for all combinations of negatvies, check if positive complement exists        
        num_negatives = len(negatives)
        for x in range(num_negatives):
            for y in range(x+1, num_negatives):
                target = -1*(negatives[x] + negatives[y])
                if target in unique_positives:
                    triplets.add(tuple(sorted([negatives[x], negatives[y], target])))
        return list(triplets)
# @lc code=end

