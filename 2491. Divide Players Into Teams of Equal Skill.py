class Solution:
    def dividePlayers(self, skill) -> int:
        data = {}
        for i in skill:
            if i not in data:
                data[i] = 0
            data[i] += 1
        target = int(sum(skill)/len(skill)*2)
        count = 0
        while data:
            j = next(iter(data))
            data[j] -= 1
            if data[j] == 0:
                data.pop(j)
            if target - j not in data:
                return -1
            data[target - j] -= 1

            count += j * (target - j)
            if data[target - j] == 0:
                data.pop(target - j)
        return count



print(Solution().dividePlayers([3,4]))
