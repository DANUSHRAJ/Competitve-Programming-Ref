#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S[100];
    int N,sum=0,i,j;
    scanf("%s%n",S,&N);
    if(N==1)
        printf("%s",S);
    else
    {
        for(i=0,j=N-1;i<N,j>=0;i++,j--)
        {
            sum+=(S[i]-'0')*(S[j]-'0');
            if(i==j-1||i==j-2)
                break;
        }
        if(N%2==1)
            sum+=S[(N-1)/2]-'0';
        printf("%d",sum);
    }
}
