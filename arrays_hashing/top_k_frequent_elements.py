# bucket sort 
# nums = [1,1,1,2,2,3], k = 2
# 0    1    2   3   4   5   6
#     [3]  [2] [1]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        count = [[] for i in range(len(nums) + 1)]
        for num,cnt in freq.items():
            count[cnt].append(num)

        res = []
        for i in range(len(count) - 1, 0, -1):
            if k == 0:
                break
            for num in count[i]:
                res.append(num)
                k -= 1
        return res

# O(n)