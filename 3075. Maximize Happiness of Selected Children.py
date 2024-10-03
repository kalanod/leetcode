class Solution:
    def maximumHappinessSum(self, happiness, k: int):
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            res += max(happiness[i] - i, 0)
        return res


print(Solution().maximumHappinessSum([2, 3, 4, 5], 1))
