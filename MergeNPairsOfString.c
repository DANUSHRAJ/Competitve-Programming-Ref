#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,k;
    scanf("%d",&N);
    char s1[1000],s2[1000];
    for(k=0;k<N;k++)
    {
        scanf("%s %s",s1,s2);
        int len1 = strlen(s1);
        int len2 = strlen(s2);
        if(len1>len2)
        {
            for(i=0;i<len2;i++)
                printf("%c%c",s1[i],s2[i]);
            for(j=len2;j<len1;j++)
                printf("%c",s1[j]);
        }
        else if(len2>len1)
        {
            for(i=0;i<len1;i++)
                printf("%c%c",s1[i],s2[i]);
            for(j=len1;j<len2;j++)
                printf("%c",s2[j]);
        }
        else
        {
            for(i=0;i<len1;i++)
                printf("%c%c",s1[i],s2[i]);
        }
        printf("\n");
    }    
}
