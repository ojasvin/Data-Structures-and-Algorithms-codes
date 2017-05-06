import math
import sys
import operator
import random
import string
class vertex:
	def __init__(self,name,i):
		self.p=None
		self.i=i
		self.d=math.inf
		self.name=name
		
class edges:
	def __init__(self,u,v,weight):
		self.u=u
		self.v=v
		self.weight=weight

	def relax(self):
		if self.u.d+self.weight<self.v.d:
			self.v.d=self.u.d+self.weight	


class Graph:
	def __init__(self,v,e):
		self.v=v
		self.e=e

	def bell(self,s):	
		s.d=0
		for i in range(0,len(self.v)-1):
			for i in range(0,len(self.e)):
				self.e[i].relax()
		for i in range(0,len(self.e)):
			if self.e[i].u.d+self.e[i].weight<self.e[i].v.d:
				return False
		self.print()
	def print(self):
		for i in range(0,len(self.v)):
			print(self.v[i].d)	



v=[]
e=[]
str=""
n=int(input("Enter number of vertices::"))
for i in range (0,n):
	v.append(vertex(input(),i))
m=int(input("Enter number of edges::"))
for i in range (0,m):
	str=input("The edge is between and the weight is::")
	v1,v2,v3=str.split(",")
	for i in range(0,len(v)):
		if v1==v[i].name:
			break
	for j in range(0,len(v)):
		if v2==v[j].name:
			break		

	e.append(edges(v[i],v[j],int(v3)))
G=Graph(v,e)
G.bell(v[0])