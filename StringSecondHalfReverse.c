#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int N,i=0;
    scanf("%s%n",S,&N);
    while(i<N/2)
        printf("%c",S[i++]);
    while(--N>=i)
        printf("%c",S[N]);
}
