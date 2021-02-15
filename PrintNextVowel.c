#include<stdio.h>
#include <stdlib.h>
int isVowel(char C)
{
    C=tolower(C);
    if(C=='a'||C=='e'||C=='i'||C=='o'||C=='u')
        return 1;
    return 0;    
}
int main()
{
    char S[1000];
    int N,i,j,flag=0;
    scanf("%s%n",S,&N);
    for(i=0;i<N-1;i++)
    {
        for(j=i+1;j<N;j++)
        {
            if(isVowel(S[j]))
            {
                printf("%c",S[j]);
                flag=1;
                break;
            }
            else
                flag=0;
        }
        if(flag==0)
            printf("%c",S[i]);
    }
    printf("%c",S[N-1]);
}
