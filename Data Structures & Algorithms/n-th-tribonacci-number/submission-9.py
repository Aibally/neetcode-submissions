class Solution:
    def tribonacci(self, n: int) -> int:
        if n<3: return [0,1,1][n]
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-2]+dp[i-1]+dp[i-3]
        return dp[n]