class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            num = nums[i]
            count[num] = count.get(num,0) + 1
        for cnt in count:
            if count[cnt] % 2 == 1: return False
        return True
        