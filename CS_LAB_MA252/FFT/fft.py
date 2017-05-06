import cmath
import math
import time
import random
def normal_multiplication(a,b):
	d=[]
	for i in range(0,len(a)):
		d.append(0)
	n=len(a)
	for k in range(0,n):
		for i in range(0,k+1):
			d[k]+=a[i]*b[k-i]
	return d			
def fft(a):
	n=len(a)
	if(n==1):
		return a
	w_n=cmath.exp(2*cmath.pi*1j/n)
	w=1
	first1=a[0:len(a):2]
	second1=a[1:len(a):2]
	first=fft(first1)
	second=fft(second1)
	y = [None] * n
	for k in range(0,n//2):
		y[k]=first[k]+w*second[k]
		y[k+n//2]=first[k]-w*second[k]
		w=w_n*w
	return y
def fft_inverse(a):
	n=len(a)
	if(n==1):
		return a
	w_n=cmath.exp(-2*cmath.pi*1j/n)
	w=1
	first1=a[0:len(a):2]
	second1=a[1:len(a):2]
	first=fft(first1)
	second=fft(second1)
	y = [None] * n
	for k in range(0,n//2):
		y[k]=first[k]+w*second[k]
		y[k+n//2]=first[k]-w*second[k]
		w=w_n*w
	y1 = [x / n for x in y]
	return y1
def point_multiplication(a,b):
	c=[x*y for x,y in zip(a,b)]
	return c

a=[]
b=[]
c=[]
d=[]
n1=input("Degree of polynomial 1 : ")
n2=input("Degree of polynomial 2 : ")
for i in range(0,int(n1)+1):
	a.append(random.randint(0,100))
for i in range(0,int(n2)+1):	
	b.append(random.randint(0,100))
if(len(b)>=len(a)):
	k=len(b)
	for i in range(len(b),2**(int(math.ceil(math.log2(k)))+1)):
		b.append(0)
	for i in range(len(a),2**(int(math.ceil(math.log2(k)))+1)):
		a.append(0)
else:
	k=len(a)
	for i in range(len(a),2**(int(math.ceil(math.log2(k)))+1)):
		a.append(0)
	for i in range(len(b),2**(int(math.ceil(math.log2(k)))+1)):
		b.append(0)
print(a)
print(b)
start1=time.time()
c=normal_multiplication(a,b)
end1=time.time()
print("**",end1-start1,"**")
print("")
print(c)
start2=time.time()
d=fft_inverse(point_multiplication(fft(a),fft(b)))
end2=time.time()
print("**",end2-start2,"**")
print(d)
