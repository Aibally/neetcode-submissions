class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n=len(nums)
        # dp[l][r] - maks monety dla przedzialu od l do r
        dp = [[0]*n for _ in range(n)]
    
        for l in range(n-1,-1,-1):
            for r in range(l+2,n):
                for i in range(l+1,r):
                    coins = dp[l][i] + dp[i][r] + nums[l]*nums[i]*nums[r]
                    dp[l][r] = max(dp[l][r],coins)
        return dp[0][n-1]
