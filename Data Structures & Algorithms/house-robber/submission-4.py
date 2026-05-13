class Solution:
    def rob(self, nums: List[int]) -> int:
        for _ in range(3):
            nums.insert(0,0)
        n = len(nums)
        dp = [0]*n
        for i in range(3,n):
            dp[i]=nums[i]+max(dp[i-2],dp[i-3])
        return max(dp[n-1],dp[n-2])
        