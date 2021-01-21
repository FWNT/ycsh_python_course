import math
def circle(r,n):
   area=r*r*math.sin(360/n/180*math.pi)*n/2
   return area
r=int(input())  
n=int(input())
print(circle(r,n))