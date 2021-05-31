#include<bits/stdc++.h>
using namespace std;
int siz[5005], rnk[5005], par[5005];
int findpar(int n){
    if(par[n]==n) return n;
    return par[n]= findpar(par[n]);
}

int main()

{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    for(int i=1; i<5005; i++){
        siz[i]=1;
        rnk[i]=1;
        par[i]=i;
    }      
    
    while(1){        
        int n, q, x=0, ans=1;
        
        map<string, int> m;
        cin>> n>> q;
        if(!n && !q) break;
        for(int i=0; i<n; i++){
        	string s;
        	cin>> s;
        	if(!m[s]) m[s]=++x;
        }
        for(int i=0; i<q; i++){
        	string s, ss;
        	cin>> s>> ss;
        	int fr1, fr2;
        	fr1= findpar(m[s]);
        	fr2= findpar(m[ss]);
        	if(fr1!=fr2){
        		if(rnk[fr1]> rnk[fr2]){
        			siz[fr1]+=siz[fr2];
        			par[fr2]=fr1;
        			ans= max(ans, siz[fr1]);
        		}
        		else if(rnk[fr2]> rnk[fr1]){
        			siz[fr2]+= siz[fr1];
        			par[fr1]= fr2;
        			ans= max(ans, siz[fr2]);
        		}
        		else{
        			siz[fr1]+=siz[fr2];
        			rnk[fr1]++;
        			par[fr2]=fr1;
        			ans= max(ans, siz[fr1]);
        		}

        	}
        }
        cout<< ans<< "\n";
        for(int i=1; i<=x; i++){
            siz[i]=1;
            rnk[i]=1;
            par[i]=i;
        }

    }
    return 0;
        
}
