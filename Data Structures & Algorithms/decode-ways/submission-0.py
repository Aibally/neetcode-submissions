class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recur(i):
            if i == len(s):
                return 1
            
            if i in memo:
                return memo[i]

            if s[i] == '0':
                return 0

            res = recur(i + 1)

            if i + 1 < len(s):
                if 10 <= int(s[i:i+2]) <= 26:
                    res += recur(i + 2)

            memo[i] = res
            return res

        return recur(0)