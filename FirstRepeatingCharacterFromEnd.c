#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[1000],C='*';
    scanf("%s",S);
    int i,j,N=strlen(S),flag=0;
    for(i=N-1;i>=0;i--)
    {
        for(j=i-1;j>=0;j--)
        {
            if(S[i]==S[j])
            {
                C=S[i];
                flag=1;
                break;
            }
        }
        if(flag==1)
            break;
    }
    if(C=='*')
        printf("-1");
    else
        printf("%c",C);    
}
