#include<stdio.h>
#include <stdlib.h>
int main()
{
    long int N;
    while(scanf("%ld",&N)==1)
    {
        if(((N/100)%10)%2==1)
        {
            printf("%ld",N);
            break;
        }
    }
}
