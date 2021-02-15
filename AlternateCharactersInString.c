#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000];
    int N,i;
    scanf("%s%n",S,&N);
    for(i=0;i<N;i+=2)
        printf("%c",S[i]);
}
