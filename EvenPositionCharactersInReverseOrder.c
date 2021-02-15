#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000];
    int N;
    scanf("%s%n",S,&N);
    if(N%2==0)
    {
        for(int i=N-1;i>=0;i-=2)
            printf("%c",S[i]);
    }
    else
    {
        for(int i=N-2;i>=0;i-=2)
            printf("%c",S[i]);
    }        
}
