#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N;
    scanf("%d",&N);
    int a[N];
    for(int i=0;i<N;i++)
        scanf("%d",&a[i]);
    for(int i=1;i<N-1;i++)
        if((a[i-1]%2==0&&a[i+1]%2==0)||(a[i-1]%2!=0&&a[i+1]%2!=0))
            printf("%d ",a[i]);
}
