#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=N-1;i>=0;i--)
    {
        printf("%d ",a[i]);
        if(a[i]%2==0)   
            i--;
        else if(a[i]%2!=0)
            i-=2;
    }
}
