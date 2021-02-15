#include<stdio.h>
#include <stdlib.h>
int main()
{
    int X,Y,N,i=1,count=0;
    scanf("%d%d%d",&X,&Y,&N);
    while(count<N)
    {
        if(i%X==0&&i%Y==0)
        {
            printf("%d ",i);
            count++;
        }
        i++;
    }
}
