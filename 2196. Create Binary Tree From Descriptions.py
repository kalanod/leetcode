# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    slov = {}

    def createBinaryTree(self, tr):

        node = TreeNode()
        a = set()
        d = set()
        self.res = []
        self.stack = []
        for i in tr:
            a.add(i[0])
            d.add(i[1])
            if i[0] not in self.slov:
                self.slov[i[0]] = [None, None]
            if i[2] == 1:
                self.slov[i[0]][0] = i[1]
            else:
                self.slov[i[0]][1] = i[1]
        root = (a - d).pop()
        r = self.createNode(root)
        return r


    def createNode(self, i):
        if not i:
            return None
        if i not in self.slov:
            return TreeNode(i, None, None)
        return TreeNode(i, self.createNode(self.slov[i][0]), self.createNode(self.slov[i][1]))


print(Solution().createBinaryTree([[39,70,1],[13,39,1],[85,74,1],[74,13,1],[38,82,1],[82,85,1]]))
