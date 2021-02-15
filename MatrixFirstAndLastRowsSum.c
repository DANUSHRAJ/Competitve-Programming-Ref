#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,sum=0;
    scanf("%d",&N);
    int a[N][N];
    for(i=0;i<N;i++)
        for(j=0;j<N;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(i==0||i==N-1)
                sum+=a[i][j];
        }
    }
    printf("%d",sum);
}
