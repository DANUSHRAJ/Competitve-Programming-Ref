#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[10];
    int N;
    scanf("%s%n",S,&N);
    for(int i=0;i<N;i++)
        printf("%d",(S[i]-'0')*2);
}
