class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        best_sum = float('-inf')
        for num in nums:
            curr_sum += num
            best_sum = max(best_sum,curr_sum)
            curr_sum = max(0,curr_sum)
        return best_sum