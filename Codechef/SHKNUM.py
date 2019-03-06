import math

t = int(input())
for i in range(0,t):
    n = int(input())
    orilog = math.log2(n)
    modilog = int(math.log2(n))
    if(n>2):
        if orilog-modilog==0:
            print(1)
        else:
            temp = int(math.log2(n))
            n = n-math.pow(2,temp)
            temp2 = int(math.log2(n))
            v1 = int(n-math.pow(2,temp2))
            v2 = int(math.pow(2,temp2+1)-n)
            ans = 0
            if v1<=v2:
                ans = v1
            else:
                ans = v2
                if temp==(temp2+1):
                    ans = ans+1
            print(ans)
    else:
        print(3-n)
