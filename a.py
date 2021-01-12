x=int(input())
a=1
for i in range(x):
  a=a+1
  if x%a==0:
     x=x/a
     print(a)
     a=1
