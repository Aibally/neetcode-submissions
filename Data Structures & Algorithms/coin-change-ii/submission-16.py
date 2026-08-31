class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        nc = len(coins)
        dp = [[0]*(amount+1) for _ in range(nc+1)]
        for i in range(nc+1):
            dp[i][0] = 1
        
        for c in range(1,nc+1):
            for a in range(1,amount+1):
                dp[c][a] = dp[c-1][a] # nie biore
                if a >= coins[c-1]:
                    dp[c][a] += dp[c][a-coins[c-1]] # biore
        
        return dp[nc][amount]