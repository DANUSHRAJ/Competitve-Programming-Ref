#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C,i,j,count=0;
    scanf("%d%d",&R,&C);
    int a[R][C];
    for(i=0;i<R;i++)
        for(j=0;j<C;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<C-1;i++)
    {
        if(a[R-1][i]==a[0][i+1])
            count++;
    }
    printf("%d",count);
}
