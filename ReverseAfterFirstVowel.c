#include<stdio.h>
#include <stdlib.h>
int isVowel(char ch)
{
    ch=toupper(ch);
    return(ch=='A'||ch=='E'||ch=='I'||ch=='O'||ch=='U');
}
int main()
{
    char S[1000];
    int N,i;
    scanf("%s%n",S,&N);
    for(i=0;S[i]!='\0'&&!isVowel(S[i-1]);i++)
        printf("%c",S[i]);
    N--;    
    while(N>=i)
    {
        printf("%c",S[N]);
        N--;
    }
}
