#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,t;
    scanf("%d",&N);
    int a[N];
    for(i=1;i<=N;i++)
        scanf("%d",&a[i]);
    if(N%2==0)
    {
        for(i=2;i<=N;i+=2)
        {
            for(j=2;j<=N;j+=2)
            {
                if(a[i]<a[j])
                {
                    t=a[i];
                    a[i]=a[j];
                    a[j]=t;
                }
            }
        }
    }
    else
    {
        for(i=1;i<=N;i+=2)
        {
            for(j=1;j<=N;j+=2)
            {
                if(a[i]<a[j])
                {
                    t=a[i];
                    a[i]=a[j];
                    a[j]=t;
                }
            }
        }
    }
    for(i=1;i<=N;i++)
        printf("%d ",a[i]);
}
