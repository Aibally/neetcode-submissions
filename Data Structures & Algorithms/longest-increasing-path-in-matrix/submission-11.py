class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        t_sorted = sorted([(matrix[i][j],i,j) for i in range(m) for j in range(n)])

        dp = [[1 for i in range(n)] for j in range(m)]

        for k in range(m*n):
            i,j = t_sorted[k][1],t_sorted[k][2]
            val = matrix[i][j]
            best = 0
            if 0 <= i-1 < m:
                if matrix[i-1][j]<val: best = max(best,dp[i-1][j])
            if 0 <= i+1 < m:
                if matrix[i+1][j]<val: best = max(best,dp[i+1][j])
            if 0 <= j-1 < n:
                if matrix[i][j-1]<val: best = max(best,dp[i][j-1])
            if 0 <= j+1 < n:
                if matrix[i][j+1]<val: best = max(best,dp[i][j+1])
            dp[i][j] = best+1
        return max(max(row) for row in dp)
