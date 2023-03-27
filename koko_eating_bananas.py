# find rate of eating
# 1 - max piles
# test the current if we can finish all banana in the constraint hour
# if we cannot, increase rate => shift left pointer
# else store rate, and decrease rate to find possible smaller rate => shift right pointer
# optimization => start at ave of pile / h
# that's the minimum rate we need to finish everything => ceil since we cannot eat partial banana
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = ceil(sum(piles) / h)
        r = max(piles)
        res = 0
        while (l <= r):
            k = (l + r) // 2
            
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            
            if hours > h:
                l = k + 1
            else:
                res = k
                r = k - 1
        return res