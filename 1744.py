
import sys
N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]
positive=[]
negative=[]
one=0
optimus=0
for i in nums:
    if i>0:
        positive.append(i)
    elif i==1:
        one+=1
    elif i<0:
        negative.append(i)

negative.sort()
positive.sort(reverse=True)
for i in range(0,len(positive),2):
    if i+1<len(positive):
       optimus+=positive[i]*positive[i+1]
    else:
        optimus+=positive[i]
for i in range(0,len(negative),2):
   if i+1<len(negative):
        optimus+=negative[i]*negative[i+1]
   else:
       optimus+=negative[i]

print(optimus)

//hjjunl: I need conflict
