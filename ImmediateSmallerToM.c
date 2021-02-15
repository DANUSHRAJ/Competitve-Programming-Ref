#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,flag=0;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    int M;
    scanf("%d",&M);
    for(i=0;i<N;i++)
    {
        for(j=i+1;j<N;j++)
        {
            if(a[i]>a[j])
            {
                int t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    if(N==2)
    {
        printf("-1");
        exit(0);
    }    
    for(i=0;i<N;i++)
    {
        if(M==a[i])
        {
            printf("%d",a[i-1]);
            flag=1;
        }
        else
        {
            continue;
        }
    }
    if(flag==1)
        exit(0);
    else
        printf("-1");
}
