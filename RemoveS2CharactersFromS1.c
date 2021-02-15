#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S1[1000],S2[1000];
    scanf("%s%s",S1,S2);
    for(int i=0;i<strlen(S1);i++)
    {
        for(int j=0;j<strlen(S2);j++)
        {
            if(S1[i]==S2[j])
                S1[i]='*';
        }
    }
    for(int i=0;i<strlen(S1);i++)
        if(S1[i]!='*')
            printf("%c",S1[i]);
}
