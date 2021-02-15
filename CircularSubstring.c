#include<stdio.h>
#include <stdlib.h>
int main()
{
    int start,end,i,N;
    char S[1000];
    scanf("%s%n",S,&N);
    scanf("%d %d",&start,&end);
    if(start<=end)
        for(i=start;i<=end;i++)
            printf("%c",S[i]);
    else if(start>end)
    {
        for(i=start;i<N;i++)
            printf("%c",S[i]);
        for(i=0;i<=end;i++)
            printf("%c",S[i]);
    }
}
