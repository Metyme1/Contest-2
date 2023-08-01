import math


def exact(s):
    i=0
    while i*i<=s:
        j=int((math.sqrt(s-i*i)))
        if i*i+ j*j==s:
            return "YES"
        i+=1
    return "NO"

n=int(input())
i=0
sum=0
while(i<n):
    line=input()
    a,b=line.split()
    a=int(a)
    b=int(b)
    sum+=(int(math.pow(a,b)))
    i+=1
out=exact(sum)
print(out)


