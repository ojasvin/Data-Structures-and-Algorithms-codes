import collections
import math
def printsol(Sol,i,j,values):
	nlist=[]
	if i==j:
		nlist.append(values[i])

	else:	
		nlist.append(values[Sol[i][j]])
		if Sol[i][j]>=1:
			nlist.append(printsol(Sol,i,Sol[i][j]-1,values))
		if Sol[i][j]<len(values)-1:	
			nlist.append(printsol(Sol,Sol[i][j]+1,j,values))

	return nlist	


def optimalbstree(sortedlist):
	Matrix=[[0 for x in range(len(sortedlist))]for y in range(len(sortedlist))]
	s=[[0 for x in range(len(sortedlist))]for y in range(len(sortedlist))]
	Sol=[[0 for x in range(len(sortedlist))]for y in range(len(sortedlist))]

	c=0
	for i in sortedlist :
		Matrix[c][c]=sortedlist[i]
		s[c][c]=sortedlist[i]
		c=c+1
	###For loop for Sum	
	for l in range(2,len(sortedlist)+1):
		for i in range(1+len(sortedlist)-l):
			j=i+l-1
			if l==2:
				s[i][j]=Matrix[i][i]+Matrix[j][j]	
			else:
				s[i][j]=Matrix[i][i]+Matrix[j][j]+s[i+1][j-1]

	for l in range(2,len(sortedlist)+1):
		for i in range(1+len(sortedlist)-l):
			j=i+l-1
			q=math.inf
			for k in range(i,j+1):
				if k==0:
					if Matrix[k+1][j]<=q:
						q=Matrix[k+1][j]
						Sol[i][j]=k
				elif k==len(sortedlist)-1:
					if Matrix[i][k-1]<=q:
						q=Matrix[i][k-1]
						Sol[i][j]=k
				else:	
					if Matrix[i][k-1]+Matrix[k+1][j]<=q:
						q=Matrix[i][k-1]+Matrix[k+1][j]	
						Sol[i][j]=k	
			
			Matrix[i][j]=s[i][j]+q	
	values=[]		
	for i in sortedlist:		
		values.append(i)
		

	nlist=printsol(Sol,0,len(sortedlist)-1,values)		
	print(nlist)
	return Matrix[0][len(sortedlist)-1]		



def main():
	slist={}
	n=int(input("Enter number of elements::"))
	for i in range(0,n):
		key=int(input())
		value=int(input())
		slist[key]=value


	od=collections.OrderedDict(sorted(slist.items()))
	print(optimalbstree(od))	



if __name__ == '__main__':
		main()	