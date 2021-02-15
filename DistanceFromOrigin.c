#include<stdio.h>
#include <stdlib.h>
int main()
{
    int X,Y;
    scanf("%d %d",&X,&Y);
    float dist=sqrt(((0+X)*(0+X))+((0+Y)*(0+Y)));
    printf("%.2f",dist);
}
