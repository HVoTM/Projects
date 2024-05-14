from typing import List
# Container with Most Water: https://www.youtube.com/watch?v=UuiTKBwPgAo&ab_channel=NeetCode

class Solution:
    def brute_force(self, height: List[int]) -> int:
        res = 0

        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res
    
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res