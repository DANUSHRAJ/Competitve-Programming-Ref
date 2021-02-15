#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[20];
    int unit,N;
    scanf("%s%n%d",S,&N,&unit);
    int ten=abs((S[N-1]-'0')%10-unit);
    for(int i=0;i<=N-2;i++)
        printf("%c",S[i]);
    printf("%d",ten);
    printf("%c",S[N-1]);
}
