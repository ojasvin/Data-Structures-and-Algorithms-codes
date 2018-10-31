#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,j,n;
	cin>>n;
	int *A;
	A=new int[n];
	for(i=0;i<n;i++)
	{
		cin>>A[i];
	}
	int sc=0,maxi=0,e=0,index,sum[n],ans=0;
	for(i=0;i<n;i++)
	{
		sc=0;
		sum[i]=0;
		maxi=0;
		e=i;
		for(index=i;index<n;index++)
		{
			maxi=max(maxi,index+A[index]);
			if(index==e)
			{
				sc++;
				e=maxi;
			}
			if(index!=i)
				sum[i]=sum[i]+sc;
		}
		cout<<sum[i]<<endl;
		ans=ans+sum[i];
	}
	cout<<ans;
}