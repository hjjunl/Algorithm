N=int(input())
bow=list(map(int, input().split()))
cnt=0
player=0
m=[]
for i in range(N):
    if bow[i]>player:
        player=bow[i]
        m.append(cnt)
        cnt=0
    else:
        cnt+=1
        if i==N-1:
            m.append(cnt)
            break
print(m)
print(max(m))

I'll try to change the code!!!! 2021-04-01-12:18
hjjunl: Please don't change the code like this. 2021-04-01-12:22
    
hyunjunl: so confussing
