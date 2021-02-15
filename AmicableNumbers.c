#include<stdio.h>
#include <stdlib.h>
int isAmicable(int M,int N)
{
    int sum=0,i;
    for(i=1;i<M;i++)
    {
        if(M%i==0)
            sum+=i;
    }
    if(sum==N)
    {
        sum=0;
        for(i=1;i<N;i++)
        {
            if(N%i==0)
                sum+=i;
        }
        if(sum==M)
            return 1;
        else
            return 0;
    }
    return 0;
}
int main()
{
    int M,N;
    scanf("%d %d",&M,&N);
    if(M==N)
        printf("NOT AMICABLE");
    else if(isAmicable(M,N))
        printf("AMICABLE");
    else
        printf("NOT AMICABLE");

}
