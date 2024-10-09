class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        taken = 0
        cur = 0
        res = 0
        for i in range(len(s)):
            if s[i] == ")":
                cur -= 1
            else:
                cur += 1
            if cur < 0:
                cur += 1
                res += 1
        return res + abs(cur)
print(Solution().minAddToMakeValid("())"))