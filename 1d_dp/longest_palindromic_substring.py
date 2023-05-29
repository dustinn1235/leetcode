class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                tmp = s[l:r + 1]
                if len(tmp) > len(res):
                    res = tmp
                l -= 1
                r += 1
        
            l,r = i,i+1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                tmp = s[l:r + 1]
                if len(tmp) > len(res):
                    res = tmp
                l -= 1
                r += 1
        return res
        


                
