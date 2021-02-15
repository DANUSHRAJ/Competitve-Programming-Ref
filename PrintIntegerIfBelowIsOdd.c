#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C;
    scanf("%d%d",&R,&C);
    int a[R][C],i,j;
    for(i=0;i<R;i++)
       for(j=0;j<C;j++)
          scanf("%d",&a[i][j]);
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            if(i==R-1)
               printf("* ");
            else if(a[i+1][j]%2!=0)
               printf("%d ",a[i][j]);
            else
               printf("* ");
        }
        printf("\n");
    }
}
