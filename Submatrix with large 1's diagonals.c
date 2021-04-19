Submatrix with large 1's diagonals

#include<stdio.h>
#include<stdlib.h>

int main()
{
int r,c,a[100][100],p=-1,q=-1,m=0;
scanf("%d %d\n",&r,&c);
for(int i=0;i<r;i++)
{
    for(int j=0;j<c;j++){
        scanf("%d ",&a[i][j]);
    }
}
for(int i=0;i<r;i++){
    for(int j=0;j<c;j++)
    {
        int d=0;
        if(a[i][j]==1)
        {
            int x=i,y=j;
            while(a[x][y]!=0)
            {
                d++;
                x++;y++;
            }
        }
        if(d>m)
        {
            m=d;
            p=i;q=j;
        }
    }
}
if(m==1||m==0){
    printf("-1");
    return 0;
}
for(int i=p;i<m+p;i++)
{
    for(int j=q;j<m+q;j++)
    {
        printf("%d ",a[i][j]);
    }
    printf("\n");
}

}