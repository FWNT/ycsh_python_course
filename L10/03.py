import random
x=int(random.randint(1,100))
while(1):
  y=int(input())
  if y>x:
    print('太大了')
  elif y<x:
    print('太小了')
  else:
    print('猜對了') 
    break