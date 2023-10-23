#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # area of rectangle = length*width
            width = right - left - 1
            if height[right] > height[left]:
                length = height[right]
                left+=1
            elif height[left] > height[right]:
                length = height[left]
                right-=1
            else:
                if height[right-1] > height[left+1]:
                    right-=1
                else:
                    left+=1
            area = width*length
            if area > max_area:
                max_area = area
        return max_area
# @lc code=end

