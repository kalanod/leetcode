class Solution:
    def getAncestors(self, n: int, edges):
        v = [False] * n
        t = [set() for i in range(n)]
        data = [[] for i in range(n)]
        for i in edges:
            t[i[1]].add(i[0])

        def f(cur, par):
            v[cur] = True
            if cur != par:
                data[par].append(cur)
            for i in t[cur]:
                if not v[i]:
                    f(i, par)

        for i in range(n):
            v = [False] * n
            f(i, i)
        return data
