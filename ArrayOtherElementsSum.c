#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,sum=0;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
    {
        scanf("%d",&a[i]);
        sum+=a[i];
    }    
    for(i=0;i<N;i++)
    {
        printf("%d ",sum-a[i]);
    }
}
