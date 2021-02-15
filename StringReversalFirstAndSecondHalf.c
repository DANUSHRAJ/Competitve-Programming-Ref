#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int N,i;
    scanf("%s%n",S,&N);
    int mid=N/2;
    for(i=mid-1;i>=0;i--)
        printf("%c",S[i]);
    if(N%2==1)
    {
        printf("%c",S[mid]);
        for(i=N-1;i>mid;i--)
            printf("%c",S[i]);
    }
    else
    {
        for(i=N-1;i>=mid;i--)
            printf("%c",S[i]);
    }
}
