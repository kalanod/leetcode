class Solution:
    def maxDistance(self, position, m: int) -> int:
        position.sort()
        return self.f(1, position[-1]-position[0], position, m)

    def f(self, left, right, data, m):
        if left == right:
            return left
        if self.check((left + right) // 2 + 1, data, m):
            return self.f((left + right) // 2 + 1, right, data, m)
        return self.f(left, (left + right) // 2, data, m)

    def check(self, dist, data, m):
        last = 0
        for i in range(len(data)):
            if i == 0 or data[i] - last >= dist:
                last = data[i]
                m -= 1
        return m < 1

print(Solution().maxDistance(position = [1,2,3,4,7], m = 3))
