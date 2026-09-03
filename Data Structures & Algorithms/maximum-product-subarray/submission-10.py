class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        max_dp = [1 for _ in range(n)]
        min_dp = [1 for _ in range(n)]
        max_dp[0] = min_dp[0] = nums[0]

        for i in range(1,n):
            a = nums[i]
            b = min_dp[i-1]*a
            c = max_dp[i-1]*a
            max_dp[i] = max(a,b,c)
            min_dp[i] = min(a,b,c)
        return max(max_dp)