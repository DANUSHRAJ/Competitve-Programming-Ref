#include<stdio.h>
#include <stdlib.h>
int isFirstandLastOdd(int N)
{
    int rem=N%10;
    while(N>=10)
    {
        N/=10;
    }    
    if(N%2==1&&rem%2==1)
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
        if(isFirstandLastOdd(a[i]))
            printf("%d ",a[i]);
    }        
}
