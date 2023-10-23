#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # area of a rectangle can be defined as length(or height)*width here
            # rectangle width is distance between points
            width = right - left
            # length is bound by the lesser value of the two
            if height[left] < height[right]:
                length = height[left]
                left+=1
            else:
                length = height[right]
                right-=1
            current_area = length*width
            if current_area > max_area:
                max_area = current_area
        return max_area
# @lc code=end

