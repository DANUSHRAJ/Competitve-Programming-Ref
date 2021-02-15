#include<stdio.h>
#include <stdlib.h>
int posSum(char C)
{
    return C-'a'+1;
}
int main()
{
    char S[100];
    int N,i,sum=0;
    scanf("%s%n",S,&N);
    for(i=0;i<N;i++)
    {
        sum+=posSum(S[i]);
    }
    printf("%d",sum);
}
