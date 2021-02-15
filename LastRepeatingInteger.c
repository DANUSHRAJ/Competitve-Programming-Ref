#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,j,flag=0;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(i=N-1;i>=0;i--)
    {
        for(j=i-1;j>=0;j--)
        {
            if(a[i]==a[j])
            {
                printf("%d",a[i]);
                flag=1;
                break;
            }
        }
        if(flag==1)
            break;
    }
}
