#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,M,i;
    scanf("%d %d",&N,&M);
    int a[N];
    for(i=0;i<N;i++)
    {
        scanf("%d",&a[i]);
        if(a[i]>M)
            printf("%d ",a[i]);
    }        
}
