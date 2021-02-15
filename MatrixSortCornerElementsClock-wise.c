#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C,i,j,k=0,corner[4]={0},t;
    scanf("%d%d",&R,&C);
    int a[R][C];
    for(i=0;i<R;i++)
        for(j=0;j<C;j++)
            scanf("%d",&a[i][j]);
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            if((i==0&&j==0) ||(i==0&&j==C-1) || (i==R-1&&j==0) || (i==R-1&&j==C-1))
                corner[k++]=a[i][j];
        }
    }
    for(i=0;i<k;i++)
    {
        for(j=0;j<k;j++)
        {
            if(corner[i]<corner[j])
            {
                t=corner[i];
                corner[i]=corner[j];
                corner[j]=t;
            }
        }
    }
    a[0][0]=corner[0];
    a[0][C-1]=corner[1];
    a[R-1][C-1]=corner[2];
    a[R-1][0]=corner[3];
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
            printf("%d ",a[i][j]);
        printf("\n");    
    }
}
