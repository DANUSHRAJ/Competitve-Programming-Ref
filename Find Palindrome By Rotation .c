#include<iostream>
using namespace std;
int noOfRotations(string s)
{
    int l=0,h=s.length()-1;
    while(h>l)
    {
        if(s[l++]!=s[h--])
            return 1;
    }
    return 0;
}
int main(int argc,char** argv)
{
    string s;
    cin>>s;
    int n=s.length(),i,count=0;
    if(noOfRotations(s)==0)
        cout<<"0";
    else    
    {    
        for(i=0;i<n;i++)
        {
            string s1=s.substr(i+1,n-i-1);
            string s2=s.substr(0,i+1);
            if(noOfRotations(s1.append(s2)))
                count+=1;
            else
                break;
        }
        if(count==n)
            cout<<"-1";
        else
            cout<<count+1;
    }  
    return 0;
}
