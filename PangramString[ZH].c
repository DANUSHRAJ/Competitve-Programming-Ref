#include<stdio.h>
#include <stdlib.h>
int isPangram(char *S)
{
    int count[26]={0},flag=0;
    for(int i=0;i<strlen(S)-1;i++)
        count[tolower(S[i])-97]++;
    for(int i=0;i<26;i++)
    {
        if(count[i]<1)
            return 0;
        else if(count[i]>=1)
            flag++;
    }
    if(flag==26)
        return 1;
}
int main()
{
    char S[1000];
    fgets(S,1000,stdin);
    if(isPangram(S))
        printf("yes");
    else
        printf("no");
}
