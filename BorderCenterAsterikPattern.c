#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,count=1;
    scanf("%d",&N);
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(i==0||j==0||i==N-1||j==N-1)
                printf("* ");
            else if(i==N/2&&j==N/2)
            {
                printf("* ");
                count++;
            }
            else
                printf("%d ",count++);
        }
        printf("\n");
    }
}
