#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[20];
    int N;
    scanf("%s%n",S,&N);
    for(int i=0;i<N;i++)
    {
        if(S[i]-'0'==8)
            printf("0");
        else if(S[i]-'0'==9)
            printf("1");
        else
            printf("%d",(S[i]-'0')+2);
    }        
}
