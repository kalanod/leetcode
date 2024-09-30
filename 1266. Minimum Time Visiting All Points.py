import math


class Solution(object):
    def __init__(self):
        self.time = 0

    def minTimeToVisitAllPoints(self, points):
        position = points[0]
        while points:
            if position == points[0]:
                points.pop(0)
                continue
            step = self.step(position, points[0])
            position = [position[0] + step[0], position[1] + step[1]]

        return self.time
        """
        :type points: List[List[int]]
        :rtype: int
        """

    def step(self, position, target):
        if target[0] > position[0]:
            if target[1] > position[1]:
                self.time += 1
                return 1, 1
            if target[1] < position[1]:
                self.time += 1
                return 1, -1
            self.time += 1
            return 1, 0
        if target[0] < position[0]:
            if target[1] > position[1]:
                self.time += 1
                return -1, 1
            if target[1] < position[1]:
                self.time += 1
                return -1, -1
            self.time += 1
            return -1, 0
        if target[1] > position[1]:
            self.time += 1
            return 0, 1
        if target[1] < position[1]:
            self.time += 1
            return 0, -1
        return 0, 0


print(Solution().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]]))
