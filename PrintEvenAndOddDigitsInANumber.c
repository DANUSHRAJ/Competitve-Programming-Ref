#include<stdio.h>
#include <stdlib.h>
void printDigits(unsigned long long int N,int rem)
{
    while(N>0)
    {
        if(N%2==rem)
            printf("%d",N%10);
        N/=10;    
    }
}
int main()
{
    unsigned long long int N;
    scanf("%llu",&N);
    printDigits(N,0);
    printf("\n");
    printDigits(N,1);
}
