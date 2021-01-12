A=[1,2,3,4,5,6,7,8,9]
B=[1,2,3,4,5,6,7,8,9]
for i in A:
  s=' '
  for x in B:
    s+=str(i)+"*"+str(x)+'='+str(i*x)+';'
  print(s)  

  
