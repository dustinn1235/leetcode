class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = 1
        curMin = 1
        res = nums[0]

        for num in nums:
            tmp = curMax
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(curMin * num, tmp * num, num)
            res = max(curMax, res)
        return res