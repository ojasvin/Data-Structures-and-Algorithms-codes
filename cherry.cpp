int recur(vector<vector<int>>& grid, int x1, int y1, int x2, int n, vector<vector<vector<int>>>&dp, int count)
{
    //Base conditions
    if(x1>n-1 || y1>n-1 || x2>n-1)return INT_MIN;
    if(dp[x1][y1][x2]!=-1)return dp[x1][y1][x2];
    if(grid[x1][y1]==-1||grid[x2][x1+y1-x2]==-1)return INT_MIN;
    
    if(x1==n-1 && y1==n-1 && x2==n-1){
        if (grid[x1][y1]==1)count++;
        //else if(grid[x1][y1]==-1)count = INT_MIN;
        dp[x1][y1][x2] = count;
        return count;
    }
    /*
    dp[x1][y1][x2] has answer to, starting from here i.e. (x1,y1)&(x2,y2) what is the maximum number of cherries you can collecta 
    */
    
    //make answer
    dp[x1][y1][x2] = max(recur(grid,x1+1,y1,x2+1,n,dp,count),
                        max(recur(grid,x1,y1+1,x2+1,n,dp,count),
                            max(recur(grid,x1+1,y1,x2,n,dp,count),
                                recur(grid,x1,y1+1,x2,n,dp,count))));
    
    //modify count
    count = dp[x1][y1][x2];
    if(x1==x2){if(grid[x1][y1]==1)count++;}
    else{
        if(grid[x1][y1]==1)count++;
        if(grid[x2][x1+y1-x2]==1)count++;
    }
    dp[x1][y1][x2] = count;
    return dp[x1][y1][x2];
    
}
class Solution 
{
public:
    int cherryPickup(vector<vector<int>>& grid) 
    {
        int n = grid.size();
        vector<vector<vector<int>>>dp(n,vector<vector<int>>(n,vector<int>(n,-1)));
        int a  = recur(grid, 0, 0 ,0, n,dp,0);
        return a>0?a:0;
    }
};