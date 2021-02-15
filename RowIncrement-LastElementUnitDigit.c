#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C,i,j;
    scanf("%d%d",&R,&C);
    int a[R][C];
    for(i=0;i<R;i++)
        for(j=0;j<C;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            printf("%d ",a[i][j]+(a[i][C-1]%10));
        }
        printf("\n");
    }
}
