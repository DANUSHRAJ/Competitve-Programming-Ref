#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[200];
    int N;
    scanf("%s%n",S,&N);
    S[N-1]='\0';
    printf("%s",&S[1]);
}
