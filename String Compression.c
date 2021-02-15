/*INPUT:
  aaabbbbcc
  OUTPUT:
  a3b4c2
  */

#include<stdio.h>
#include <stdlib.h>
int main()
{
    int i,j,count=0;
    char S[10000],S1[10000];
    scanf("%s",S);
    strcpy(S1,S);
    for(i=0;i<strlen(S);i++)
    {
        count=0;
        for(j=i;j<strlen(S);j++)
        {
            if(S[i]==S1[j])
            {
                count++;
                S1[j]='*';
            }
            else
                break;
        }
        if(count>0)
            printf("%c%d",S[i],count);
    }
}
