# two pointer l,r. Keep track of maxL and maxR. Shift by min(maxL,maxR)
class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxL = height[0]
        maxR = height[-1]

        res = 0
        while (l < r):
            if maxL <= maxR:
                res += maxL - height[l]
                l += 1
                maxL = max(maxL, height[l])
            else:
                res += maxR - height[r]
                r -= 1
                maxR = max(maxR, height[r])
        return res