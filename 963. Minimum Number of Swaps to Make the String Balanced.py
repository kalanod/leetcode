class Solution:
    def minSwaps(self, s: str) -> int:
        taken = 0
        cur = 0
        res = 0
        for i in range(len(s)):
            if s[i] == "]":
                cur -= 1
            else:
                cur += 1
            if cur < 0:
                taken -= 1
                cur += 2
                res += 1
        return (res + taken + cur) // 2
print(Solution().minSwaps("[]"))