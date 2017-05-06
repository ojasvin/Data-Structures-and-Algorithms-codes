import math

def maxheapify(a,i,n):
  l=left(i)
  r=right(i)
  largest=i
  if l<n and a[l]>a[i]:
    largest=l
  if r<n and a[largest]<a[r]:
    largest=r  
  if largest!=i:
    a[i],a[largest]=a[largest],a[i]
    maxheapify(a,largest,n)

def left(i):
  return 2*i+1

def right(i):
  return 2*i+2

def parent(i):
  return (i-1)//2
    
def buildmaxheap(a):
  for i in range (len(a)//2-1,-1,-1):
    maxheapify(a,i,len(a))




class priortyy:
  def __init__(self,val,n):
    self.val=val
    self.n=n
    buildmaxheap(self.val)
  
  def insert(self,x):
    self.val[self.n]=-math.inf
    #print(self.val)
    self.n=self.n+1
    self.increasekey(self.n-1,x)
    

  def increasekey(self,i,x):
    self.val[i]=x
    z=i
    while z>0 :
      maxheapify(self.val,parent(z),self.n)
      z=(z-1)//2

  def maximum (self):
    print(self.val[0])
  
  def removemaximum (self):
    self.val[0],self.val[self.n-1]=self.val[self.n-1],self.val[0]
    self.n=self.n-1
    self.val.pop()
    maxheapify(self.val,0,self.n)


print("Enter number of elements:::")
n=int(input())
m=[0 for i in range(n)]
print("Enter the list::")
for i in range (0,n):
  m[i]=int(input())
y=priortyy(m,n)
print(y.val)
print("Enter the number of values to be inserted")
k=int(input())
for i in range (0,k):
  print("Enter the value to be inserted:::")
  j=int(input())
  y.val.append(0)
  y.insert(j)
print(y.val)
y.maximum()
y.removemaximum()
print(y.val)
 
