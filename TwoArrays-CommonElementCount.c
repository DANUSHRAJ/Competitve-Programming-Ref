#include<stdio.h>
#include <stdlib.h>
int main()
{
    int M,N,i,j,count=0;
    scanf("%d %d",&M,&N);
    int a[M],b[N];
    for(i=0;i<M;i++)
        scanf("%d",&a[i]);
    for(j=0;j<N;j++)
        scanf("%d",&b[j]);
    for(i=0;i<M;i++)
    {
        for(j=0;j<N;j++)
        {
            if(a[i]==b[j])
            {
                b[j]=-1;
                count++;
                break;
            }
        }
    }
    printf("%d",count);

}
