#include<iostream>
#include<bits/stdc++.h>
using namespace std;

bool isSafe(vector<int >cg,vector<vector<int >>adj,int col ,int node)
{
    for(int i=0;i<adj.size();i++)
    {
        if(i!=node && cg[i]==col && adj[node][i]==1  )
        {
            return false;
        }
    }
    return true;
}
bool solve(vector<vector<int>>& adj, vector<int>& cg, int m, int n, int node) {
    if (node == n) {
        return true;
    }
    for (int i = 1; i <= m; i++) {
        if (isSafe(cg, adj, i, node)) {
            cg[node] = i;
            if (solve(adj, cg, m, n, node + 1)) {
                return true;
            }
            cg[node] = 0; // Backtrack
        }
    }
    return false;
}
int main()
{
    int V;
    
    vector<vector<int >>adj;  
    
    adj={
        {0, 1 ,1 ,0},
        {1 ,0 ,1 ,1},
        {1, 1, 0, 1},
        {0 ,1 ,1 ,0}
    };
    vector<int >cg(adj.size(),0);
    solve(adj,cg,4,adj.size(),0);
    for(int i=0;i<cg.size();i++)
    {
        cout<<i<<" - "<<cg[i]<<endl;
    }

    return 0;
}