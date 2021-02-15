#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N;
    scanf("%d",&N);
    if(N%2==0)
        for(int i=N-1;i>=1;i-=2)
            printf("%d ",i);
    else
        for(int i=N-1;i>=2;i-=2)
            printf("%d ",i);
}            
