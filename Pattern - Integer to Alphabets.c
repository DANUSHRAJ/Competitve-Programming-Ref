#include<stdio.h>
#include <stdlib.h>
char inttoalpha(int X)
{
    char alphabet[26]={'Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y'};
    return alphabet[X];
}
int main()
{
    int N,i=0,j;
    scanf("%d",&N);
    int a[N];
    if(N==26)
        printf("Z");
    else
    {
        while(N>0)
        {
            a[i++]=N%26;
            N/=26;
        }
        for(j=i-1;j>=0;j--)
            printf("%c",inttoalpha(a[j]));
    }
    return 0;
}
