#include<stdio.h>
#include <stdlib.h>
int main()
{
    int M,N,i,j,count=0,max=0,r;
    scanf("%d %d",&M,&N);
    int a[M][N];
    for(i=0;i<M;i++)
        for(j=0;j<N;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<M;i++)
    {
        count=0;
        for(j=0;j<N;j++)
        {
            if(a[i][j]%2!=0)
                count++;
        }        
        if(count>max)
        {
            max=count;
            r=i;
        }
    }
    for(i=0;i<N;i++)
        printf("%d ",a[r][i]);
}
