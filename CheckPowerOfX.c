include<stdio.h>
#include <stdlib.h>
int isPower(int N,int X)
{
    if(N==1&&X==1)
            return 1;
    int i=1;
    while(i<N)
        i*=X;
    return (i==N);    
}
int main()
{
    int N,X;
    scanf("%d%d",&N,&X);
    if(isPower(N,X))
        printf("YES");
    else
        printf("NO");
}
