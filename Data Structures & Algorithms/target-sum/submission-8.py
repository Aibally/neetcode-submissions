class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total=sum(nums)
        offset=total
        T = [[0] * (2*total+1) for _ in range(len(nums)+1)]

        if abs(target) > total:
            return 0

        T[0][offset] += 1

        for i in range(1,len(nums)+1):
            for j in range(2*total+1):
                if T[i-1][j] != 0:
                    num = nums[i-1]
                    T[i][j-num] += T[i-1][j]
                    T[i][j+num] += T[i-1][j]
        return T[len(nums)][target+offset]
        