#include<stdio.h>
#include <stdlib.h>
int main()
{
   char S[1000];
   int i,j,n,ct=0;
   scanf("%s%n",S,&n);
   for(i=1;i<n;i++)
   {
       if(S[i]==S[i-1])
       {
           while(S[i]==S[i-1]&&i<n)
               i++;
           ct++;
       }
   }
   printf("%d",ct);
}
