#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[10];
    int N;
    scanf("%s%n",S,&N);
    for(int i=0;i<N;i++)
    {
        if(i==0)
        {
            if((S[1]-'0')%2!=0)
                printf("%c",S[0]);
        }
        if(i==N-1)
        {
            if((S[N-2]-'0')%2!=0)
                printf("%c",S[N-1]);
        }
        else
        {
            if(((S[i-1]-'0')%2!=0)&&((S[i+1]-'0')%2!=0))
                printf("%c",S[i]);
        }
    }
}
