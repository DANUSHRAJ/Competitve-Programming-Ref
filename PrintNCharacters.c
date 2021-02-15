#include<stdio.h>
#include <stdlib.h>
int main()
{
    char C;
    int N,i;
    scanf("%c%d",&C,&N);
    for(i=1;i<=N;i++)
    {
        if(C=='Z')
        {
            printf("%c",C);
            C='A';
        }
        else if(C=='z')
        {
            printf("%c",C);
            C='a';
        }
        else
        {
            printf("%c",C);
            C+=1;
        }
    }
}
