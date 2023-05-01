# we only care if our max frequency character go up because that's when our res change.
# we always need a larger maxF to get a new better result
# 6 - 4 <= 2 (res = 6)
# If we have a length of 7, therefore we need to have maxF of 5 in order to take 7. 7 - 5 <= 2
# if maxF is less than current maxF, for example 3. Then 7-3 is not <= 2. Which we cannot update res.
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxF = 0
        res = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            maxF = max(maxF, count[s[r]])

            lengthOfWindow = r - l + 1
            while (lengthOfWindow - maxF > k):
                count[s[l]] -= 1
                l += 1
                lengthOfWindow = r - l + 1
            
            res = max(res, lengthOfWindow)
        return res