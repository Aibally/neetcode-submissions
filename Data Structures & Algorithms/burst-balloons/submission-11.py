class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1] # laczny profit jezeli ity balon jest ostatnim przebitym
        cache = {}
        def dfs(l,r):
            if (l,r) in cache: return cache[(l,r)]
            if l+1==r: return 0
            ans = 0
            for i in range(l+1,r):
                coins = (
                    dfs(l,i) +
                    dfs(i,r) +
                    nums[l]*nums[i]*nums[r]
                )
                ans = max(ans,coins)
            cache[(l,r)] = ans
            return ans
        return dfs(0,len(nums)-1)
            