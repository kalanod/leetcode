class Solution:
    def getAncestors(self, n: int, edges):
        visited = [False] * n
        t = [set() for i in range(n)]
        res = [[] for i in range(n)]
        for i in edges:
            t[i[1]].add(i[0])


        def dfs(cur, par):
            visited[cur] = True
            if cur != par:
                res[par].append(cur)
            for i in t[cur]:
                if not v[i]:
                    dfs(i, par)

        for i in range(n):
            visited = [False] * n
            dfs(i, i)
        return res
