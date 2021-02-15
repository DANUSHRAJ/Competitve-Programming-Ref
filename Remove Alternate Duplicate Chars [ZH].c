#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000],S1[1000];
    fgets(S,1000,stdin);
    int i,j,k=0;
    strcpy(S1,S);
    for(i=0;i<strlen(S);i++)
    {
        k=0;
        for(j=0;j<strlen(S);j++)
        {
            if(S1[i]==S[j])
            {
                k++;
                if(k%2==0)
                {
                    S1[j]='*';
                }
            }
        }
    }
    for(i=0;i<strlen(S);i++)
    {
        if(S1[i]!='*')
            printf("%c",S1[i]);
    }
}
