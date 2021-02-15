#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,a;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
        scanf("%d",&a);
        printf("%d ",2*(a%10));
    }
}
