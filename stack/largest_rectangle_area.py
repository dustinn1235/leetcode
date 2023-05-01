class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights)):
            start = i
            while (len(stack) != 0 and stack[-1][1] > heights[i]):
                topI, topH = stack.pop()
                area = topH * (i - topI)
                res = max(res, area)
                start = topI
            stack.append((start,heights[i]))

        while (len(stack) != 0):
            topI, topH = stack.pop()
            area = topH * (len(heights) - topI)
            res = max(res, area)
        return res