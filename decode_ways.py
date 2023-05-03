class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        def solve(s):
            if s in dp:
                return dp[s]

            if s[0] == "0":
                dp[s] = 0
                return 0 

            if len(s) == 1:
                dp[s] = 1
                return 1
            
            if len(s) == 2:
                if int(s) > 26:
                    if int(s) % 10 == 0:
                        return 0
                    else:
                        return 1
                else:
                    if int(s) % 10 == 0:
                        return 1
                    else:
                        return 2
            
            if int(s[:2]) <= 26:
                dp[s] = solve(s[1:]) + solve(s[2:])
            else:
                dp[s] = solve(s[1:])
            return dp[s]  

        return solve(s)   