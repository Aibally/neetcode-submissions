class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [(nums[i],nums[i]) for i in range(n)]

        for i in range(1,n):
            curr = nums[i]
            last_min, last_max = dp[i-1]
            options = (last_min*curr,last_max*curr,curr)
            dp[i] = (min(options),max(options))
        return max([max(a,b) for a,b in dp])