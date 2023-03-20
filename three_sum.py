# two sum sorted for every num in nums
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while (l < r):
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    # skip duplicate
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        return res