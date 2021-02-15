#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C;
    scanf("%d %d",&R,&C);
    int i,j,a;
    for(i=0;i<R;i++)
    {
        for(j=0;j<C;j++)
        {
            scanf("%d",&a);
            if(i==0||j==0||i==R-1||j==C-1)
                printf("%d ",a);
            else
                printf("- ");
        }
        printf("\n");
    }
}
