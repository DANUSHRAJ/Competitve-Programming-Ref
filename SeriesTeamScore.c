#include<stdio.h>
#include <stdlib.h>
int main()
{
   int a[100],i=0,k,N,counta=0,countb=0;
   while((scanf("%d",&a[i]))==1)
   {
       i++;
   }
   N=i/2;
   for(k=0;k<N;k++)
   {
       if(a[k]<a[N+k])
        countb+=3;
       else if(a[k]>a[N+k])
        counta+=3;
        else if(a[k]==a[N+k])
        {
            counta+=1;
            countb+=1;
        }
   }
   printf("%d %d",counta,countb);
}