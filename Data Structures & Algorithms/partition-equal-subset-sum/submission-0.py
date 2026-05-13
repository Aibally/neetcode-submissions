class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum3 = sum(nums)
        if sum3 % 2 != 0: return False
        def rec(sum2,i,n):
            if sum2==0: return True
            if i==n or sum2<0: return False
            return rec(sum2-nums[i],i+1,n) or rec(sum2,i+1,n)
        return rec(sum3//2,0,len(nums))
        