import math
mod = 1000000007

def expo(x,y,f):
    result = 1
    x = x%f
    while y:
        if y & 1:
            result = (result*x)%f
        x = (x*x)%f
        y >>= 1
    return result

t = int(input())
for i in range(0,t):
    a,b,n = map(int, input().split())
    a = int(a)
    b = int(b)
    n = int(n)
    cfact = abs(a-b)
    ori_ans =(expo(a,n,mod)+expo(b,n,mod))%mod
    if a==b:
        print(ori_ans)
    else:
        oth_ans = (expo(a,n,cfact)+expo(b,n,cfact))%cfact
        print(math.gcd(cfact,oth_ans)%mod)
