#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100],a[100];
    int N,i,k=0;
    scanf("%s%n",S,&N);
    for(i=0;i<N;i++)
        if(i%2==0)
            a[k++]=S[i];
    k-=1;
    for(i=0;i<N;i++)
        if(i%2==0)
            S[i]=a[k--];
    printf("%s",S);
}
