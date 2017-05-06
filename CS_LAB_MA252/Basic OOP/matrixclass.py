class matrix:

  def __init__(self,m,n,val):#constructor to initialize degree and values
    self.m=m
    self.n=n
    self.val=val
    
    
  def __add__(self,mi):#to add to matrix of any int size

    r=matrix(self.m,self.n,[[0 for j in range(self.n)] for i in range(self.m)])
    if self.m!=mi.m or self.n!=mi.n:
      print("error::")
    else:
      for i in range(0,self.m):
        for j in range(0,self.n):      
          r.val[i][j]=self.val[i][j]+mi.val[i][j]
          #print(r.val[i][j])
    return r   


  def __mul__(self,mi):
  	
    r=matrix(self.m,self.n,[[0 for j in range(self.n)] for i in range(self.m)])
    if self.n!=mi.m:
      print("error:::")
    else:
      for i in range(0,self.m):
        for j in range(0,mi.n):
          for k in range(0,self.n):      
            r.val[i][j]=r.val[i][j]+self.val[i][k]*mi.val[k][j]      

    return r



print("enter the degree of two matrices::")
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())   
print("enter values::")
ma1 = [[0 for j in range(y1)] for i in range(x1)]
ma2 = [[0 for j in range(y2)] for i in range(x2)]

for i in range (0,x1):
  for j in range (0,y1):
    ma1[i][j]=int(input())      

for i in range (0,x2):
  for j in range (0,y2):
    ma2[i][j]=int(input())

     
m1=matrix(x1,y1,ma1)       
m2=matrix(x2,y2,ma2)     
print(m1.val)
print(m2.val)
m3=m1+m2
m4=m1*m2
print("Sum::")
print(m3.val)
print("Product::")
print(m4.val)
