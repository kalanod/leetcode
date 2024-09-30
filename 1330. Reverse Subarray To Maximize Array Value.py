class Solution(object):
    def maxValueAfterReverse(self, nums):
        min_val = abs(nums[1] - nums[0])
        min_pos = 0
        vals = []
        for i in range(1, len(nums)):
            vals.append([abs(nums[i] - nums[i-1]), i])
            if abs(nums[i] - nums[i-1]) < min_val:
                min_val = abs(nums[i] - nums[i-1])
                min_pos = i
        for i in vals:
            