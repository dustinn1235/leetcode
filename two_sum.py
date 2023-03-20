# hashmap to check occurance. Look for comp number in hashmap

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    map = {}

    for i in range(len(nums)):
      comp = target - nums[i]
      
      if comp in map:
        return [i,map[comp]]
      else:
        map[nums[i]] = i