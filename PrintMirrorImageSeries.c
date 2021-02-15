#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    for(i=N;i>=1;i--)
        printf("%d ",i);
    for(i=2;i<=N;i++)
        printf("%d ",i);
}
