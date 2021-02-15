#include <iostream>
using namespace std;
int main(int argc, char** argv)
{
    string S;
    int N,i,j,flag=0;
    cin>>S;
    cin>>N;
    string S1[N];
    for(i=0;i<N;i++)
        cin>>S1[i];
    for(i=0;i<S.size();i++)
    {
        flag=0;
        for(j=0;j<N;j++)
        {
            if(S[i]==S1[j][0])
            {
                cout<<S1[j];
                flag=1;
                S1[j]='*';
                break;
            }
        }
        if(flag==0)
            cout<<S[i];
        cout<<"\n";    
    }
    cout<<"\n";
}
