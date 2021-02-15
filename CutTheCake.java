#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,a,arr[100],k=0,max,t,sum=0;
    scanf("%d",&N);
    while(scanf("%d",&a)==1)
    {
        arr[k++]=a;
    }
    max=arr[0];
    for(int i=1;i<k;i++)
    {
        t=arr[i]-arr[i-1];
        if(max<t)
            max=t;
        sum+=t;    
    }
    sum+=arr[0];
    if(max<(N-sum))
        max=N-sum;
    printf("%d",max);    
}
