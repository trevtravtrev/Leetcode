#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        BAD solution (should use hash dictionary to store values and search from instead of list)
        for index1, num in enumerate(numbers):
            search_num = target - num
            if search_num in numbers:
                index2 = numbers.index(search_num)
                # means there's duplicates (i.e. [0, 0]), iterate to next index to get duplicate
                if index2 == index1:
                    index2+=1
                return [index1+1, index2+1]
        """
        """
        Can also use binary search, very fast, but greater space complexity
        """
        # TWO POINTER SOLUTION
        # O(N) time (slightly slower than binary O(logN)), better space complexity than binary
        # index of left and right value
        left, right = 0, len(numbers)-1
        # will iterate until left and right value "meet in the middle" (==)
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            # increase sum by smallest amount possible, hence next left number since increasing sorted
            elif sum < target:
                left+=1
            # if sum is greater than target, use next smallest largest number to try to not go over target
            else:
                right-=1


# @lc code=end

