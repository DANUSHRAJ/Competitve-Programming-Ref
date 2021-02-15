#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,t;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=0;i<N;i++)
    {
        for(j=i+1;j<N;j++)
        {
            if(a[i]>a[j])
            {
                t=a[i];
                a[i]=a[j];
                a[j]=t;
            }
        }
    }
    printf("%d %d",a[0],a[N-1]);
}
