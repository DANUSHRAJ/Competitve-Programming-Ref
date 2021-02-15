#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=0;i<N-1;i++)
        if(a[i]%10==a[i+1]%10)
            printf("%d ",a[i]);
}
