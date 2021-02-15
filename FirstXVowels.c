#include<stdio.h>
#include <stdlib.h>
int main()
{
    int X,N,i,count=0;
    char S[1000];
    scanf("%d %s",&X,S);
    N=strlen(S);
    for(i=0;i<N;i++)
    {
        if(S[i]=='a'||S[i]=='e'||S[i]=='i'||S[i]=='o'||S[i]=='u')
        {
            printf("%c",S[i]);
            count++;
            if(count==X)
                break;
        }    
    }
}
