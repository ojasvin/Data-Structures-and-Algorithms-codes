def printlcs(b,X,i,j):
	if i==0 or j==0:
		return
	if b[i][j]=="proceed":
		printlcs(b,X,i-1,j-1)
		print(X[i-1])
	elif b[i][j]=="^":
		printlcs(b,X,i-1,j)
	else:
		printlcs(b,X,i,j-1)



def lcs(A,B):
	la=len(A)
	lb=len(B)

	w, h = la, lb;
	c = [[0 for x in range(h+1)] for y in range(w+1)] #c is length of lcs
	b = [[0 for x in range(h+1)] for y in range(w+1)] 
	
	for i in range(0,w):
		for j in range(0,h):
			if A[i]==B[j]:
				c[i+1][j+1]=c[i][j]+1
				b[i+1][j+1]="proceed"
			elif c[i][j+1]>=c[i+1][j]:
				c[i+1][j+1]=c[i][j+1]
				b[i+1][j+1]="^"
			else:
				c[i+1][j+1]=c[i+1][j]
				b[i+1][j+1]=" "

	printlcs(b,A,la,lb)			
	return c[la][lb]

A=str(input("Enter the first dna strand:::"))
B=str(input("Enter the second dna strand:::"))
print("The length of longest common subsequence is {}".format(lcs(A,B)))

