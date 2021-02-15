#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C,M,N,a,i,j;
    scanf("%d %d %d %d",&R,&C,&M,&N);
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            scanf("%d",&a);
            if(j!=N-1&&i!=M-1)
                printf("%d ",a);
        }
        printf("\n");
    }    
}
