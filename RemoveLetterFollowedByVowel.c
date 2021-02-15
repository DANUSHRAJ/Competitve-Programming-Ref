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
    scanf("%s",S);
    for(int i=0;i<strlen(S)-1;i++)
    {
        if(isVowel(S[i+1]))
            S[i]='$';
    }
    for(int i=0;i<strlen(S);i++)
        if(S[i]!='$')
            printf("%c",S[i]);
}
