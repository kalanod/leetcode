class Solution:
    MOD = 10 ** 9 + 7

    def fSumOfK(self, nums, n, target):
        currSum = window = total = count = 0
        i = 0
        for j in range(n):
            currSum += nums[j]
            window += nums[j] * (j - i + 1)
            while target < currSum:
                window -= currSum
                currSum -= nums[i]
                i += 1
            total += window
            count += j - i + 1
        return count, total % self.MOD

    def findSum(self, nums, n, k):
        right = sum(nums)
        left = min(nums)
        while left <= right:
            mid = (left + right) // 2
            if self.fSumOfK(nums, n, mid)[0] >= k:
                right = mid - 1
            else:
                left = mid + 1
        count, total = self.fSumOfK(nums, n, left)
        return (total - left * (count - k)) % self.MOD

    def rangeSum(self, nums, n, left, right):
        res = (self.findSum(nums, n, right) - self.findSum(nums, n, left - 1)) % self.MOD
        return res