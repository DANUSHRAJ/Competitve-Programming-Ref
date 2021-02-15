#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int count=0;
    while(scanf("%s",S)==1)
    {
        if(!strcmp(S,"a")||!strcmp(S,"an")||!strcmp(S,"the")||!strcmp(S,"a,")||!strcmp(S,"an,")||!strcmp(S,"the,")||!strcmp(S,"a.")||!strcmp(S,"an.")||!strcmp(S,"the."))
            count++;
    }
    printf("%d",count);
}
