#include<stdio.h>
#include <stdlib.h>
int main()
{
    long long int N;
    int X,Xdigit=1;
    scanf("%lld %d",&N,&X);
    while(X--)
    {
        Xdigit*=10;
    }
    int last=N%Xdigit;
    while(N>Xdigit)
    {
        N/=10;
    }
    printf("%s",(last==N)?"Yes":"No");

}
