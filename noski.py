a = int(input())
b = int(input())
c = int(input())
d = int(input())
if max(a, b)+1 <= min(c, d)+1:
    print(max(a, b)+1, 1)
elif max(c, d)+1 <= min(a,b)+1:
    print(1, max(c, d)+1)
else:
    print(min(a, b) + 1 if min(a, b) + 1 <= max(a,b) else min(a, b), min(c, d) + 1)
