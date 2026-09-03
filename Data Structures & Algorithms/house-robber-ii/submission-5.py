class Solution:
    def robHelper(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2: return max(nums)
        dp=[0]*n
        dp[0],dp[1] = nums[0],max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:return nums[0]
        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))
    