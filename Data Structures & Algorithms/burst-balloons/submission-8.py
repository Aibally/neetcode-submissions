from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def recursion(l, r):
            if l + 1 == r:
                return 0

            ans = 0

            for i in range(l + 1, r):
                coins = (
                    recursion(l, i)
                    + recursion(i, r)
                    + nums[l] * nums[i] * nums[r]
                )

                ans = max(ans, coins)

            return ans

        return recursion(0, len(nums) - 1)
