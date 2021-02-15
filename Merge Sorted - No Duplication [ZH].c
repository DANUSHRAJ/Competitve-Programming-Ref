#include<stdio.h>
#include <stdlib.h>
int main()
{
    int M,N,i,j,t;
    scanf("%d %d",&M,&N);
    int a[M+N];
    for(i=0;i<M+N;i++)
        scanf("%d",&a[i]);
    for(i=0;i<M+N;i++)
    {
        for(j=i+1;j<M+N;j++)
        {
            if(a[i]>a[j])
            {
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    for(i=0;i<M+N;i++)
    {
        for(j=i+1;j<M+N;j++)
        {
            if(a[i]==a[j])
                a[j]='*';
        }
    }
    for(i=0;i<M+N;i++)
    {
        if(a[i]!='*')
            printf("%d ",a[i]);
    }
}
