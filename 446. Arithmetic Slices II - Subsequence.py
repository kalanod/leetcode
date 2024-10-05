class Solution:
    def numberOfArithmeticSlices(self, nums) -> int:
        dc = [{} for i in range(len(nums))]
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                c = nums[i] - nums[j]
                res += dc[j].get(c, 0)
                dc[i][c] = dc[j].get(c, 0) + 1 + dc[i].get(c, 0)
        return res
print(Solution().numberOfArithmeticSlices([2,4,6,8,10]))
