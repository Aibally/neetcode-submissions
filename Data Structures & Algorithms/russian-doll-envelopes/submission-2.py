class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        dp = [1]*n
        envelopes.sort()

        for i in range(1,n):
            w1,h1 = envelopes[i]
            for j in range(i):
                w2,h2 = envelopes[j]

                if w2<w1 and h2<h1:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

        