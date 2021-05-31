#include<bits/stdc++.h>
using namespace std;
int siz[100005], rnk[100005], par[100005];
int findpar(int n){
    if(par[n]==n) return n;
    return par[n]= findpar(par[n]);
}

int main()

{

    int test;
    scanf("%d", &test);
    for(int k=0;k<test;k++){
        if(!k){
            for(int i=1; i<100006; i++){
                siz[i]=1;
                rnk[i]=1;
                par[i]=i;
            }
        }
        int n;
        map<string, int> m;
        cin>> n;
        int x=0, frnd=0;
        for(int i=0; i<n; i++){
            string s, ss;
            cin>> s>> ss;
            if(!m[s]) m[s]=++x;
            if(!m[ss]) m[ss]= ++x;
            int fr1, fr2;
            fr1=findpar(m[s]);
            fr2=findpar(m[ss]);
            if(fr1!= fr2){
                if(rnk[fr1] > rnk[fr2]){
                    siz[fr1] +=siz[fr2];
                    par[fr2]= fr1;
                }
                else if(rnk[fr1] < rnk[fr2]){
                    siz[fr2] += siz[fr1];
                    par[fr1]= fr2;
                }
                else{
                    siz[fr1] += siz[fr2];
                    rnk[fr1]++;
                    par[fr2]= fr1;
                }
            }
            //else cout<< frnd<< "\n";
            cout<< siz[findpar(m[s])]<< "\n";


        }
        for(int i=1; i<=x; i++){
            siz[i]=1;
            rnk[i]=1;
            par[i]=i;
        }

    }



    return 0;
}

