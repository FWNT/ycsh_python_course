x=int(input())
y=int(input())
a=1
c=1
for i in range(x):
  a=a+1
  if x%a==0 and y%a==0:
     c=a
print(c)
