from itertools import combinations


class Solution:
    def subsets(self, nums):
        res = set()
        for i in range(len(nums)+1):
            for j in combinations(nums, i):
                res.add(j)
        return [list(i) for i in res]


print(Solution().subsets([1, 2, 3]))
