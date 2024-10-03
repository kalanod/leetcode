class Solution:
    def nearestPalindromic(self, n: str):
        res = []
        if int(n) <= 10:
            return str(int(n) - 1)
        r = list(n)
        for i in range(len(r) // 2):
            r[-i - 1] = r[i]
        res.append(int("".join(r)))
        cof = 10**(len(n)//2)
        while cof > 0:
            r = list(str(int(n) // 10 * 10 - 1 * cof))
            for i in range(len(r) // 2):
                r[-i - 1] = r[i]
            res.append(int("".join(r)))
            r = list(str((int(n) // 10) * 10 + 1 * cof))
            for i in range(len(r) // 2):
                r[-i - 1] = r[i]
            res.append(int("".join(r)))
            cof //= 10
        return str(sorted(filter(lambda x: x != int(n), res),
                          key=lambda x: (abs(int(n) - x), x))[0])


print(Solution().nearestPalindromic("1283"))
