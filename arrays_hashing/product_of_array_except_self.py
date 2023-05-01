# calculate prefix and postfix array
# nums = [1,2,3,4]
# pre = [1,1,2,6]
# post = [24,12,4,1]
# ans = [24,12,8,6]
# time post and pre together

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            left[i] = left[i-1] * nums[i-1]

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue        
            right[i] = right[i+1] * nums[i+1]

        for i in range(len(nums)):
            left[i] *= right[i]
        
        return left