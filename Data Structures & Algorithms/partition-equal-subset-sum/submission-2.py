class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum3 = sum(nums)
        if sum3 % 2 != 0: return False

        target=sum3//2
        n = len(nums)
        memo = [[False] * (target+1) for _ in range(n)]

        def rec(target,i):
            if target==0: return True
            if i==n or target<0: return False

            if memo[i][target]:
                return memo[i][target]

            memo[i][target] = rec(target-nums[i],i+1) or rec(target,i+1)
            return memo[i][target]

        return rec(target,0)