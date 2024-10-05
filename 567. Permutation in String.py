class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(sorted(list(s1)))
        s2 = list(sorted(list(s2)))
        for i in range(len(s2) - len(s1) + 1):
            f = 1
            for j in range(len(s1)):
                if s2[i+j]!=s1[j]:
                    f=0
                    break
            if f:
                return True
        return False



print(Solution().checkInclusion(s1="ab", s2="eidboaoo"))
