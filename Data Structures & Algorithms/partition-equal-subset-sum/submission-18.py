class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: return False
        target = sum(nums) // 2

        # czy dla danej sumy na danym idx wlacznie dalej dojde do celu
        dp = [[-1]*(target+1) for _ in range(len(nums))]

        def dfs(i=0,curSum=0):
            if curSum == target: return True
            if i == len(nums) or curSum > target: return False
            if dp[i][curSum] != -1: return dp[i][curSum]

            a = dfs(i + 1, curSum + nums[i])
            b = dfs(i + 1, curSum)
            
            dp[i][curSum] = a or b
            return dp[i][curSum]

        return dfs()