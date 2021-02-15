#include<stdio.h>
#include <stdlib.h>
int isEven(int N)
{
    int count=0;
    while(N>0)
    {
        N/=10;
        count++;
    }
    if(count%2==0)
        return 1;
    return 0;    
}
int main()
{
    int N,i;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
    {
        scanf("%d",&a[i]);
        if(isEven(a[i]))
            printf("%d ",a[i]);
    }
}
