#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int N,I;
    scanf("%s%n%d",S,&N,&I);
    for(int i=I-1;i<N;i++)
        printf("%c",S[i]);
}
