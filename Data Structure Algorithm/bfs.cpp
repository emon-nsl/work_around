#include <bits/stdc++.h>
using namespace std;
#define MAX 100000
std::vector<int> edges[MAX];
std::vector<int> cost[MAX];
std::map<int, vector<int> > edg;
int level[MAX] = {0};
std::queue<int> q;
bool vis[MAX] = {0};
void bfs(int source){
	// cout<< "inside bfs"<<endl;
	q.push(source);
	level[source] = 0;
	vis[0] = 1;
	while(!q.empty()){
		int working_node = q.front();
		q.pop();
		cout<< working_node<< "working_node"<<endl;
		for(int i=0; i<edg[working_node].size(); i++){
			// q.push(edg[working_node][i]);
			cout<< edg[working_node][i]<< "working_node of edg "<<endl;
			// break;
			if(!vis[edg[working_node][i]]){
				vis[edg[working_node][i]] = 1;
				level[edg[working_node][i]] = level[working_node] + 1;
				cout<< "level ================"<< level[edg[working_node][i]]<<endl;
				q.push(edg[working_node][i]);
			}
			// break;
		}
		// break;
	}
}
int main()
{
	int node_no, edge_no;
	cin>> node_no;
	// for(int i=0; i<node_no; i++)
	// 	level[i] = 1<<30;
	// for(int i=0; i<node_no; i++)
	// 	cout<<level[i]<<endl;

	for(int i=1; i<=node_no; i++){
		int x, y;
		cin>> x>> y;
		edg[x].push_back(y);
		edg[y].push_back(x);
		cout<<i<<endl;
	}
	cout<<"here we are"<<endl;
	bfs(0);
	cout<< "after bfs"<<endl;
	for(int i=1; i<=node_no; i++)
		cout<< level[i]<<endl;


	return 0;
}