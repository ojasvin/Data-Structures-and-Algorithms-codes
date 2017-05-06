import math

def minheapify(a,i,n):
  l=left(i)
  r=right(i)
  largest=i
  if l<n and a[l].val<a[i].val:
    largest=l
  if r<n and a[largest].val>a[r].val:
    largest=r  
  if largest!=i:
    a[i],a[largest]=a[largest],a[i]
    minheapify(a,largest,n)

def left(i):
  return 2*i+1

def right(i):
  return 2*i+2

def parent(i):
  return (i-1)//2
    
def buildminheap(a):
  for i in range (len(a)//2-1,-1,-1):
    minheapify(a,i,len(a))




class priorty:
  def __init__(self,val,n):
    self.val=val
    self.n=n
    buildminheap(self.val)
  
  def insert(self,x):
    self.val[self.n].key=math.inf
    #print(self.val)
    self.n=self.n+1
    self.dkey(self.n-1,x)
    
  def find(self,x):
  	
  

  def dkey(self,i,x):
    self.val[i]=x
    z=i
    while z>0 :
      minheapify(self.val,parent(z),self.n)
      z=(z-1)//2

  def minimum (self):
    return self.val[0]

  def empty(self):
  	if self.val==None:
  		return True
  	else:
  		return False	

  def removeminimum (self):
    self.val[0],self.val[self.n-1]=self.val[self.n-1],self.val[0]
    self.n=self.n-1
    self.val.pop()
    minheapify(self.val,0,self.n)

'''
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
 '''
