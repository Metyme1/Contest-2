# n=int(input())
# li=list(map(int,input().split()))[:n]
# li.sort()
# li.pop(0)
# li.pop(-1)

# a=max(li)
# b=min(li)

# print(b,a)


t = int(input())

mark = [int(i) for i in input().split()]
mark.sort()
print(mark[1], mark[-2])