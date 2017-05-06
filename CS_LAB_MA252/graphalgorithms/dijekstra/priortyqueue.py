import math

def minheapify(a,i,n):
  l=left(i)
  r=right(i)
  largest=i
  if l<n and a[l].d<a[i].d:
    largest=l
  if r<n and a[largest].d>a[r].d:
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
  
    
  def empty(self):
    if len(self.val)==0:
      return True
    else:
      return False 

  def dkey(self,i,x):
    self.val[i].d=x
    z=i
    while z>0 :
      minheapify(self.val,parent(z),self.n)
      z=(z-1)//2

  def minimum (self):
    return self.val[0]
  
  def removeminimum (self):
    self.val[0],self.val[self.n-1]=self.val[self.n-1],self.val[0]
    self.n=self.n-1
    self.val.pop()
    minheapify(self.val,0,self.n)

