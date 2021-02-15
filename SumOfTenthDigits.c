#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    int a[N],sum=0;
    for(i=0;i<N;i++)
    {
        scanf("%d",&a[i]);
        sum+=(a[i]/10)%10;
    }
    printf("%d",sum);
}
