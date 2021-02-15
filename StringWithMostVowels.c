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
    char S1[1000],S2[1000];
    scanf("%s %s",S1,S2);
    int count1=0,count2=0;
    for(int i=0;i<strlen(S1);i++)
        if(isVowel(S1[i]))
            count1++;
    for(int i=0;i<strlen(S2);i++)
        if(isVowel(S2[i]))
            count2++;
    if(count1>count2)
        printf("%s",S1);
    else if(count1<count2)
        printf("%s",S2);
    else if(count1==count2)
    {
        if(strlen(S1)>strlen(S2))
            printf("%s",S1);
        else
            printf("%s",S2);
    }
}
