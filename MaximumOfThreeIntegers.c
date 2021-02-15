#include<stdio.h>
#include <stdlib.h>
int isMax(int a,int b,int c)
{
    
    if(a>b&&a>c)
        return a;
    else if(b>c)
        return b;
    else
        return c;
}
int main()
{
    int N,i,max;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=0;i<N;i+=3) 
    {
        max=isMax(a[i],a[i+1],a[i+2]);
        printf("%d ",max);    
    }
}
