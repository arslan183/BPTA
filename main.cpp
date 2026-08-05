/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include<vector>
void vertexCover(vector <int> &gr)


int main()
{
    int n,m;
    std::cout<<"Enter n and m: ";
    std::cin>>n>>m;
    std::vector <int> adj[n+1];
    
    
    
    std::cout<<"Enter pairs: ";
    for(int i=0; i<m; i++){
        int u,v;
        std::cin>> u>>v;
        adj[u].push_back(v);
        
        //adj[v].push_back(u);
    }
    std::cout<<"Adjacency list\n";
    for(int i=1; i<=n;i++){
        std::cout<<i<<":";
        for(int g : adj[i]){
            std::cout<<g<<" ";
        }
      std::cout<<std::endl;
    }
     
vertexCover(adj)
    return 0;
}