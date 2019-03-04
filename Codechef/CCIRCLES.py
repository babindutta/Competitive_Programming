# Coded by Babin Dutta
# Coded in Python


import math
import bisect

n, q = map(int, input().split())
x = []
y = []
r = []
a = []
b = []
for i in range(0, n):
    n1, n2, n3 = map(float, input().split())
    x.append(n1)
    y.append(n2)
    r.append(n3)


def dist(i, j):
    d = math.pow((x[i]-x[j]),2) + math.pow((y[i] - y[j]),2)
    return math.sqrt(d)


for i in range(0, n - 1):
    for j in range(i + 1, n):
        if x[i] != x[j] or y[i] != y[j] or r[i] != r[j]:
            d = dist(i,j)
            small = min(r[i],r[j])
            big = max(r[i],r[j])
            if d>small+big:
                a.append(math.ceil(d-big-small))
            elif d<big-small:
                a.append(math.ceil(big-d-small))
            else:
                a.append(0)
            b.append(math.floor(d+small+big)+1)
a = sorted(a)
b = sorted(b)
for i in range(0,q):
    k = int(input())
    more = bisect.bisect(a,k)
    less = bisect.bisect(b,k)
    print(more-less)
