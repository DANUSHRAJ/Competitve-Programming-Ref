#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000];
    int N,K,i;
    scanf("%s%n%d",S,&N,&K);
    int count=K/N,r=K%N;
    for(i=0;i<count;i++)
        printf("%s",S);
    for(i=0;i<r;i++)    
        printf("%c",S[i]);
}
