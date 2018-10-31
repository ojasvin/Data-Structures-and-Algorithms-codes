#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	while(t>0)
	{
		t--;
		int r1,r2;
		cin>>r1;
		cin>>r2;
		int n,i,j;
		cin>>n;
		string text;
		cin>>text;
		vector<int> cells(n+1,-1);
		cells[1]=0;
		for(i=2;i<=n;i++)
		{
			if(cells[i]==-1)
			{
				cells[i]=1;
				for(j=i+i;j<=n;j=j+i)
				{
					cells[j]=0;
				}
			}
		}
		for(i=2;i<=n;i++)
		{
			cells[i]=cells[i]+cells[i-1];
		}
		queue<pair<int,int> >q;
		std::vector<bool> visited(n+1,false);
		if(text[0]!='*')
		{
			q.push(make_pair(1,0));
			visited[1]=true;
		}
		else
			return -1;
		int A;
		while(!q.empty())
		{
			pair<int,int> t=q.front();
			if(t.first==n && text[t.first-1]!='*')
				return t.second;
			q.pop();
			if(!visited[t.first+1] && text[t.first]!='*')
			{
				if(t.first+1==n)
					return t.second+1; 
				q.push(make_pair(t.first+1,t.second+1));
				visited[t.first+1]=true;
			}
			if(!visited[t.first+2] && text[t.first+1]!='*')
			{
				if(t.first+2==n)
					return t.second+1;
				q.push(make_pair(t.first+2,t.second+1));
				visited[t.first+2]=true;
			}
			A=cells[t.first];
			if((float)A/i >= (float)r1/r2 && t.first+A<=n )
			{
				if(!visited[t.first+A] && text[t.first+A-1]!='*')
				{
					if(t.first+A==n)
						return t.second+1;
					q.push(make_pair(t.first+A,t.second+1));
					visited[t.first+A]=true;
				}
			}
		}
		return -1;
	}
	
}