#include<stdio.h>
#include <stdlib.h>
int main()
{
    int C,R,i,j,b=0;
    scanf("%d %d",&C,&R);
    int a[C][R];
    for(i=0;i<C;i++)
    {
        for(j=0;j<R;j++)
        {
            scanf("%d",&a[i][j]);
        }
    }    
    for(j=0;j<R;j++)
    {
        b=a[0][j];
        for(i=1;i<C;i++)
        {
            if(a[i][j]>b)
              b=a[i][j];
        }
        printf("%d ",b);
        b=0;
    }
}
