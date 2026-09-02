class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if n>=k+maxPts or k==0: return 1
        dp = [0 for _ in range(n+1)]
        dp[0] = 1.0
        res=0
        for i in range(1,n+1):
            start = max(0, i-maxPts)
            end = min(i, k)
            
            if start < end:
                dp[i] = sum(dp[start:end]) / maxPts
            
            if i >= k:
                res += dp[i]
        return res