class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [1]*n
        for i in range(n):
            num=nums[i]
            for j in range(0,i):
                if nums[j]<num: dp[i] = max(dp[j]+1,dp[i])
        return max(dp)