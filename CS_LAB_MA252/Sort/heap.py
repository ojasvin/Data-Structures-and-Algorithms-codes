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
    
def buildmaxheap(a):
  for i in range (len(a)//2-1,-1,-1):
    maxheapify(a,i,len(a))
    
def heapsort(a):
  buildmaxheap(a)   
  s=len(a)
  for i in range (0,len(a)-1):
    a[0],a[s-1]=a[s-1],a[0]
    s=s-1
    maxheapify(a,0,s)
  print(a)
  
a=[5,13,2,25,7]
heapsort(a)
