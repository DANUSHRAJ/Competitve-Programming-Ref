#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S1[1000],S2[1000];
    scanf("%s %s",S1,S2);
    int i,j,count=0;
    for(i=0;i<strlen(S1);i++)
    {
        if(S1[i]-S2[i]==1||S1[i]==S2[i]||S2[i]-S1[i]==1)
            count++;
    }
    if(count==strlen(S1))
        printf("Yes");
    else
        printf("No");
}
