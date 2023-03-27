# 3 4 5 6 7 0 1 2 
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left sorted portion
            # 3 - 6
            if nums[l] <= nums[m]:
                # if target = 1 which is target < nums[l] (1 < 3) => search right
                # if target = 7 which is target > nums[m] => search right
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                # if target = 4 which is target >= nums[l] and target <= nums[m] => search left
                else:
                    r = m - 1
            # right sorted portion
            # 3 - 0
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1 
        return -1
