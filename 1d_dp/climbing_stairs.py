class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
            
        memo = [-1] * (n+1)
        for i in range(4):
            memo[i] = i

        for i in range(4, n+1):
            memo[i] = memo[i-1] + memo[i-2]    
        return memo[n]    