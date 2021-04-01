#1931 ctrl+ k +c / ctrl + k + u
#import sys
#def greedy(m):
#    mcount=0
#    start=0
#    for time in m:
#        if time[0]>=start:
#            start=time[1]
#            mcount+=1
#    return mcount

#n=int(sys.stdin.readline())
#line=[]
#for i in range(n):
#    start, end= map(int,sys.stdin.readline().split())
#    line.append((start,end))

#line= sorted(line, key=lambda i: i[0])
#line= sorted(line, key=lambda i : i[1])
#print(greedy(line))
import sys
N=int(sys.stdin.readline())

for i in range(N):
    m,n =map(int, sys.stdin.readline().split())
    A=1
    k=n-m
    
    while n>k:
        A*=n
        n-=1
    while m>1:
        A/=m
        m-=1

    print(A)
