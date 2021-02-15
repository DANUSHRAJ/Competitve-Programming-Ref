#include<stdio.h>
#include <stdlib.h>
int main()
{
    int N,i,sum=0,avg;
    scanf("%d",&N);
    int a[N];
    for(i=0;i<N;i++)
    {
        scanf("%d",&a[i]);
        sum+=a[i];
    }
    avg=sum/N;
    int max=1000,ans;
    for(i=0;i<N;i++)
    {
        
        if(abs(a[i]-avg)<=max)
        {
            max=abs(a[i]-avg);
            ans=a[i];
        }
    }
    printf("%d",ans);
}
