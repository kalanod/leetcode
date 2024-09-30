class Solution(object):
    def numSteps(self, s):
        a = int(s, 2)
        t = 0
        while a!=1:
            t+=1
            if a % 2 == 1:
                a+=1
            else:
                a /= 2
        return t