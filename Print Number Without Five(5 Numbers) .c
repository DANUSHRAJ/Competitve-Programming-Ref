#include<stdio.h>
#include <stdlib.h>
int main()
{
    int a[10000],i,N;
    while(1)
    {
        N=-1;
        scanf("%d",&N);
        if(N==-1)
            break;
        a[i++]=N;
    }
    printf("%d",a[3]);    
}
