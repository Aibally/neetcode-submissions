class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0]=0;dp[1]=0
        
        for i in range(n):
            if i + 1 <= n:
                dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            if i + 2 <= n:
                dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])
        return dp[n]