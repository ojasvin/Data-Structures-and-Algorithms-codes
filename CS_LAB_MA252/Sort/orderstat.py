
from random import randint

def randompartition(a,p,r):
	q=randint(p,r)
	print("fuck::",q)
	a[r],a[q]=a[q],a[r]
	return partition(a,p,r)

def partition(a,p,r):
	q=a[r]
	i=p-1
	for j in range(p,r-1): 
		if a[j]<=a[r]:
			i=i+1
			a[i],a[j]=a[j],a[i]

	a[i+1],a[r]=a[r],a[i+1]
	return i+1

def quickselect(a,p,r,i):
	if p==r:
		return a[p]
	q=randompartition(a,p,r)	
	k=q-p+1
	if i==k:
		return a[q]
	elif i<k:
		return quickselect(a,p,q-1,i)
	else:
		return quickselect(a,q+1,r,i-k)


a=[]
print("enter number of elements and then the array::")
n=int(input())
for i in range(0,n):
	a.append(int(input()))
m=int(input("Enter i th smalllest integer to be printed:::"))
x=quickselect(a,0,n-1,m)	
print(x)








