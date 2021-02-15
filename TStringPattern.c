#include<stdio.h>
#include <stdlib.h>
int main()
{
    char S1[100],S2[100];
    scanf("%s %s",S1,S2);
    int i,j,row,col;
    printf("%s\n",S1);
    for(i=strlen(S1)-1;i>=0;i--)
    {
        if(S2[0]==S1[i])
        {
            j=i;
            break;
        }
    }
    for(row=1;row<=strlen(S2)-1;row++)
    {
        for(col=0;col<=strlen(S1)-1;col++)
        {
            if(col!=j)
                printf("-");
            else
                printf("%c",S2[row]);
        }
        printf("\n");
    }
}
