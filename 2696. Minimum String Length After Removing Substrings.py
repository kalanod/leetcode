class Solution:
    def minLength(self, s: str) -> int:
        stack = ["1"]
        for i in s:
           stack.append(i)
           while stack[-1] == "B" and stack[-2] == "A" or stack[-1] == "D" and stack[-2] == "C":
               stack.pop(-1)
               stack.pop(-1)
        return len(stack)-1