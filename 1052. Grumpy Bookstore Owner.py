class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        ans = 0

        maxPos = 0

        a = [sum(customers[i] * grumpy[i] for i in range(minutes))]
        max = a[0]
        for i in range(1, len(customers) - minutes + 1):
            a.append(a[i - 1] - customers[i - 1] * grumpy[i - 1] + customers[i + minutes - 1] * grumpy[i + minutes - 1])
            if a[i] > max:
                max = a[i]
                maxPos = i
        for i in range(len(customers)):
            if not grumpy[i] or maxPos <= i < maxPos + minutes:
                ans += customers[i]
        return ans


print(Solution().maxSatisfied(customers=[3, 8, 8, 7, 1], grumpy=[1, 1, 1, 1, 1], minutes=3))
