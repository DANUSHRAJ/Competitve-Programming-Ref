#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,no=1,k;
    scanf("%d",&N);
    int a[N][2*N];
    for(i=N;i>=1;i--)
    {
        k=0;
        for(j=0;j<N-i;j++)
            a[N-i][k++]=0;
        for(j=N;j>N-i+1;j--)
        {
            a[N-i][k++]=no++;
            a[N-i][k++]=0;    
        }
        a[N-i][k++]=no++;
        for(j=0;j<N-i;j++)
            a[N-i][k++]=0;
    }
    for(i=0;i<N;i++)
    {
        if(i%2==0)
        {
            for(j=0;j<(2*N)-1;j++)
            {
                if(a[i][j]==0)
                    printf("*");
                else
                    printf("%d",a[i][j]);
            }
        }
        else
        {
            for(j=(2*N)-2;j>=0;j--)
            {
                if(a[i][j]==0)
                    printf("*");
                else
                    printf("%d",a[i][j]);
            }
        }
        printf("\n");
    }
}
