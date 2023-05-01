# hashmap to check frequency

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}

        for num in nums:
            if (num not in map.keys()):
                map[num] = 1
            else:
                return True
        return False