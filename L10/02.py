import math
r=int(input())
n=int(input())
a=360/n/180*math.pi
x=r*r*math.sin(a)*n/2
print(x)