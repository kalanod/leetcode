import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
a = {abs(x3-x1) if y1 <= y3 <= y2 else -1:"W",
     abs(x3-x2) if y1 <= y3 <= y2 else -1:"E",
     abs(y3-y1) if x1 <= x3 <= x2 else -1:"S",
     abs(y3-y2) if x1 <= x3 <= x2 else -1:"N",
     math.sqrt(abs(x3-x1)**2+abs(y3-y1)**2): "SW",
     math.sqrt(abs(x3-x1)**2+abs(y3-y2)**2): "NW",
     math.sqrt(abs(x3-x2)**2+abs(y3-y1)**2): "SE",
     math.sqrt(abs(x3-x2)**2+abs(y3-y2)**2): "NE"}
e = list(a.keys()).copy()
for i in e:
    if i == -1:
        a.pop(i)
print(a[min(a)])
