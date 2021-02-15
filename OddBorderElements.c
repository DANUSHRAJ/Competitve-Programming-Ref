#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,a;
    scanf("%d",&N);
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            scanf("%d",&a);
            if(i==0||j==0||i==N-1||j==N-1)
                if(a%2==1)
                    printf("%d ",a);
        }
    }
}
