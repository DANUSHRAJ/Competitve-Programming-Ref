#include<stdio.h>
#include <stdlib.h>
int main()
{
    unsigned long long int N;
    int oddsum=0,evensum=0;
    scanf("%llu",&N);
    while(N>0)
    {
        if(N%2==0)
        {
            oddsum+=N%10;
        }
        else 
        {
            evensum+=N%10;
        }
        N/=10;
    }
    printf("%d",abs(oddsum-evensum));
}
