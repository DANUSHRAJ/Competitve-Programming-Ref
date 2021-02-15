#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,a[100],i,k=0,prod=1;
    while(1)
    {
        N=-1;
        scanf("%d",&N);
        if(N==-1)
            break;
        a[k++]=N;    
    }
    for(i=0;i<k;i++)
        prod*=a[i];
    for(i=0;i<k;i++)
        printf("%d ",(prod/a[i]));
}
