#include<stdio.h>
#include <stdlib.h>
int main()
{
    int R,C,i,j,a,b;
    scanf("%d%d",&R,&C);
    for(i=0;i<R;i++)
    {
        a=i+1;
        b=(2*R)-i;
        for(j=0;j<C;j++)
        {
            if(i%2==0)
            {
                if(j%2==0)
                {
                    printf("%d ",a);
                    a+=(2*R);
                }
                else
                {
                    printf("%d ",b);
                    b+=(2*R);
                }
            }
            else
            {
                if(j%2==0)
                {
                    printf("%d ",a);
                    a+=(2*R);
                }
                else
                {
                    printf("%d ",b);
                    b+=(2*R);
                }
            }
        }
        printf("\n");
    }
}
