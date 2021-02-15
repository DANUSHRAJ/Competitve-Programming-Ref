#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,k;
    scanf("%d",&N);
    int a[N];
    char arr[1000][1000];
    for(i=0;i<N;i++)
        scanf("%d ",&a[i]);
    int max=a[0];
    for(i=1;i<N;i++)
        if(a[i]>max)
            max=a[i];
    for(i=0;i<N;i++)
    {
        for(j=0;j<max-a[i];j++)
            arr[i][j]='-';
        for(k=max-a[i];k<max;k++)
            arr[i][k]='*';
    }
    for(i=0;i<max;i++)
    {
        for(j=0;j<N;j++)
            printf("%c",arr[j][i]);
        printf("\n");    
    }
}
