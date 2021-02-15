#include<stdio.h>
#include <stdlib.h>
int main()
{
    int X,Y;
    scanf("%d %d",&X,&Y);
    if(X%10>Y%10)
        printf("%d",X);
    else if(X%10<Y%10)
        printf("%d",Y);
    else if(X%10==Y%10)
    {
        if(X>Y)
            printf("%d",X);
        else
            printf("%d",Y);
    }
}
