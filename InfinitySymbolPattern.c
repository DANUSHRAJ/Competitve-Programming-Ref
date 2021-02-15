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
        printf("%d ",a[i][i]);
    for(i=N-2;i>=1;i--)
        printf("%d ",a[i][N-1]);
    for(i=0;i<N;i++)
    {
        for(j=N-1;j>=0;j--)
            if(i+j==N-1)
                printf("%d ",a[i][j]);
    }
    for(i=N-2;i>=0;i--)
        printf("%d ",a[i][0]);
}
