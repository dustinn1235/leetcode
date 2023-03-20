# two pointers. a + b < target => shift a. If a + b > target shift b.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = numbers
        l = 0
        r = len(nums) - 1
        
        while (l < r):
            print(l,r)
            total = nums[l] + nums[r]
            if total == target:
                return [l+1,r+1]
            elif target < total:
                r -= 1
            else:
                l += 1