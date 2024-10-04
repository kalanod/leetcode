
from itertools import combinations
a = [23,2,4,6,6]
b = list(combinations(a, 4))
for i in b:
    if sum(i)%7==0:
        print(i)