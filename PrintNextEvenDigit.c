#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000];
    scanf("%s",S);
    for(int i=0;i<strlen(S);i++)
    {
        if((S[i]-'0')%2!=0)
            printf("%d",(S[i]-'0'+1)%10);
        else
            printf("%d",(S[i]-'0'+2)%10);
    }
}
