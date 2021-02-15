#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N;
    scanf("%d",&N);
    int a[N];
    for(int i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(int i=1;i<N;i++)
        if(a[i]%10==a[i-1]%10)
            printf("%d ",a[i]);
}
