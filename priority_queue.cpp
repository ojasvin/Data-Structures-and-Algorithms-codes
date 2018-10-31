#include <bits/stdc++.h>
using namespace std;
int main()
{
	int i,temp,n,m,team,sums=0,j;
	std::vector<int> v;
	cin>>n;
	cin>>m;
	cin>>team;
	for(i=0;i<n;i++)
	{
		cin>>temp;
		v.push_back(temp);
	}
	priority_queue<int> a,b;
	for(i=0;i<m;i++)
	{
		a.push(v[i]);
	}
	i--;
	for(j=v.size()-1;j>=0;j--)
	{
		if(j<=i)
			break;
		b.push(v[j]);
	}
	j++;
	int k,temp1,temp2;
	for(k=0;k<team;k++)
	{
		temp1=0;
		temp2=0;
		if(!a.empty())
		{
			temp1=a.top();
		}
		if(!b.empty())
		{
			temp2=b.top();
		}
		if(temp1>=temp2 && !a.empty())
		{	
			a.pop();
			if(i+1<j)
			{
				a.push(v[i+1]);
				i++;
			}
		}
		else if(temp1<temp2 && !b.empty())
		{
			b.pop();
			if(i<j-1)
			{
				b.push(v[j-1]);
				j--;
			}
		}
		sums=sums+max(temp1,temp2);
	}
	cout<<sums;
	return 0;
}