class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=amount
        dp = [0]*(n+1) # min coins needed to change n$
        for i in range(1,n+1):
            best = float('inf')
            for coin in coins:
                if i-coin >= 0:
                    best = min(dp[i-coin]+1, best)
            dp[i] = best

        return dp[n] if isinstance(dp[n],int) else -1