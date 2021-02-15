#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,M,i;
    scanf("%d %d",&N,&M);
    int a[N];
    for(i=1;i<=N;i++)
        scanf("%d",&a[i]);
    for(i=M;i<=N;i+=M)
        printf("%d ",a[i]);
}
