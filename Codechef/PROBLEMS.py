import math

realmp = []
p,s = map(int,input().split())
for i in range(p):
        mp = []
        cnt = 0
        a = list(map(int,input().split()))
        b = list(map(int,input().split()))
        for k in range(0,s):
            mp.append((a[k],b[k]))
        mp = sorted(mp)
        for k in range(0,s-1):
            if mp[k][1]>mp[k+1][1]:
                cnt = cnt+1
        realmp.append((cnt,i+1))
realmp = sorted(realmp)
for i in range(p):
    print(realmp[i][1])
