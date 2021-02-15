#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,k,lsum=0,rsum=0;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=0;i<N;i++)
    {
        for(j=0;j<i;j++)
            lsum+=a[j];
        for(k=i+1;k<N;k++)
            rsum+=a[k];
        if(lsum==rsum)
            printf("%d ",a[i]);
        lsum=0;rsum=0;    
    }
}
