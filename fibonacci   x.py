F=[0,1]
n=int(input())
for n in range(2,n+1):
  Fn=F[n-1]+F[n-2]
  F.append(Fn)
print(F[n])