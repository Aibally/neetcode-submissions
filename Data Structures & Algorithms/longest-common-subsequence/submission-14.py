class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        best = -1

        for i in range(m):
            l1 = text1[i]
            for j in range(n):
                l2 = text2[j]

                if l1==l2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])

                best = max(best,dp[m][n])
        return best