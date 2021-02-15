#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j;
    scanf("%d",&N);
    char first[N][50],last[N][50],t[50];
    for(i=0;i<N;i++)
        scanf("%s %s",first[i],last[i]);
    for(i=0;i<N;i++)
    {
        for(j=i+1;j<N;j++)
        {
            if(strcmp(last[i],last[j])>0)
            {
                strcpy(t,first[i]);
                strcpy(first[i],first[j]);
                strcpy(first[j],t);
                strcpy(t,last[i]);
                strcpy(last[i],last[j]);
                strcpy(last[j],t);
            }
        }
    }
    for(i=0;i<N;i++)
        printf("%s %s\n",first[i],last[i]);
}
