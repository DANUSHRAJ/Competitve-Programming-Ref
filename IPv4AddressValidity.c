#include<stdio.h>
#include <stdlib.h>
int main()
{
    int IP,m=0,c=0;
    while(scanf("%d.",&IP)!=-1)
    {
        if(IP<0||IP>255)
        {
            m=1;
            break;
        }
        c++;
        if(c>=5)
        {
            m=1;
            break;
        }
    }
    if(m==1||c<4)
        printf("Invalid");
    else
        printf("Valid");
}
