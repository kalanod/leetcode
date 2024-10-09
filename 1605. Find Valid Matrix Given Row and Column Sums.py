class Solution:
    def restoreMatrix(self, rowSum, colSum):
        res = [[] for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                res[i].append(min(rowSum[i], colSum[j]))
                rowSum[i] -= res[i][j]
                colSum[j] -= res[i][j]
        return res
print(Solution().restoreMatrix(rowSum = [3,8], colSum = [4,7]))