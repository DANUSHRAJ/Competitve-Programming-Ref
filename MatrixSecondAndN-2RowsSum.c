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
            if(i==1||i==N-2)
            {
                sum+=a[i][j];
            }    
        }
    }
    printf("%d",sum);        
}
