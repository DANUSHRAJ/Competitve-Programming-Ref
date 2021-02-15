#include<stdio.h>
#include <stdlib.h>
int main()
{
    int X,Y,Z;
    scanf("%d%d%d",&X,&Y,&Z);
    for(int i=X;i<=Y;i++)
        printf("%d ",i);
    printf("\n");
    for(int i=Y;i<=Z;i++)
        printf("%d ",i);
}
