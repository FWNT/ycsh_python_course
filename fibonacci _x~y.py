F=[0,1]
n=int(input())
m=int(input())
B=[]
for m in range(2,m+1):
  a=F[m-1]+F[m-2]
  F.append(a)
for n in range(n-1):
  F.pop(0)
print(F)