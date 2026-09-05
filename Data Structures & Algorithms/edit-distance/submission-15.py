class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        cache={}
        def dfs(i, j):
            if (i,j) in cache: return cache[(i,j)]
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                ame = dfs(i+1,j+1)
                cache[(i,j)] = ame
                return ame
            res = min(dfs(i + 1, j), dfs(i, j + 1))
            res = min(res, dfs(i + 1, j + 1))
            cache[(i,j)] = res+1
            return res + 1

        return dfs(0, 0)