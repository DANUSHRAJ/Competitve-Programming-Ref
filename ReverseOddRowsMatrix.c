#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j;
    scanf("%d",&N);
    int a[N][N];
    for(i=0;i<N;i++)
        for(j=0;j<N;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<N;i++)
    {
        if(i%2==0)
        {
            for(j=N-1;j>=0;j--)
                printf("%d ",a[i][j]);
        }
        else
        {
            for(j=0;j<N;j++)
                printf("%d ",a[i][j]);
        }
        printf("\n");
    }
}
