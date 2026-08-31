class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def recursion(i=0,s=0):
            if (i,s) in cache: return cache[(i,s)]
            if amount==s: return 1
            if s>amount: return 0
            if i==len(coins): return 0

            a = recursion(i,s+coins[i])
            b = recursion(i+1,s)

            res = a+b
            cache[(i,s)] = res
            return res
        return recursion()