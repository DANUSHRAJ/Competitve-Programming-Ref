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
    char S[100];
    int N,i,c=0;
    scanf("%s%n",S,&N);
    for(i=1;i<N-1;i++)
    {
        if(isVowel(S[i-1])&&isVowel(S[i+1]))
            printf("%c",S[i]);
        else
            c++;
    }
    if(c==N-2)
        printf("-1");
}
