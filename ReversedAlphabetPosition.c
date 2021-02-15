#include<stdio.h>
#include <stdlib.h>
char revValue(char C)
{
    if(islower(C))
        return 97+26-(C-'a'+1);
    else if(isupper(C))
        return 65+26-(C-'A'+1);
}
int main()
{
    char S[1000];
    int i,N;
    scanf("%s%n",S,&N);
    for(i=0;i<N;i++)
        printf("%c",revValue(S[i]));
}
