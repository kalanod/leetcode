class Solution:
    def twoSum(self, nums, target: int):
        s = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in s:
                return [i, s[target-nums[i]]]
