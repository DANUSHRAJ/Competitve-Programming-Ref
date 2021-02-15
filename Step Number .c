#include<stdio.h>
#include <stdlib.h>
#include<math.h>
int main()
{
    long long int N,a[100000],i,k=0,flag=0;
    scanf("%lld",&N);
    while(N>0)
    {
        a[k++]=N%10;
        N/=10;
    }
    for(i=k-2;i>=1;i--)
    {
        if(abs(a[i]-a[i+1])==1&&abs(a[i]-a[i-1])==1)
            flag=1;
        else
        {
            flag=0;
            break;
        }
    }
    if(flag==1)
        printf("YES");
    else
        printf("NO");
}
