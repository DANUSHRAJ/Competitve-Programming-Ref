#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    if(N%2==0)
    {
        for(i=N;i>0;i-=2)
            printf("%d ",i);
        for(i=1;i<N;i+=2)
            printf("%d ",i);
    }
    else
    {
        for(i=N-1;i>0;i-=2)
            printf("%d ",i);
        for(i=1;i<=N;i+=2)
            printf("%d ",i);
    }
}
