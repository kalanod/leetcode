class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.child = {}

        def add(self, val):
            self.child[val] = val

    def __init__(self):
        self.prefixes = {}

    def longestCommonPrefix(self, arr1, arr2):
        for i in arr1:
            self.put(str(i), 0, self.prefixes)

        maxx = 0
        for i in arr2:
            maxx = max(maxx, self.findMatch(str(i), 0, self.prefixes))
        return maxx

    def put(self, j, i, node):
        if i == len(j):
            return
        if j[i] not in node:
            node[j[i]] = self.Node(j[i])
        self.put(j, i + 1, node[j[i]].child)

    def findMatch(self, num, pos, node):
        if pos == len(num) or num[pos] not in node:
            return pos
        return self.findMatch(num, pos + 1, node[num[pos]].child)

