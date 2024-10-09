class Solution:
    def secondHighest(self, s: str) -> int:
        a = [-1, -1]
        for i in s:
            if i.isdigit() and int(i) > a[0] and int (i) not in a:
                a[0] = int(i)
                a.sort()
        return a[0]
print(Solution().secondHighest("sjhtz8344"))