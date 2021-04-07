N=int(input())
anw=0
left=0
if N==1 or N==3:
    anw= -1
elif (N%5)%2==0:
    left=(N%5)//2
    anw=(N//5+left)
else:
    anw=(N//5-1+(N%5+5)//2)
print(anw)

#test commit
