#include<stdio.h>
#include <stdlib.h>
int arePalindrome(char *S1,char *S2)
{
    int N1=strlen(S1);
    int N2=strlen(S2);
    char *temp;
    void *ptr;
    if(N1!=N2)
       return 0;
    temp=(char *)malloc(sizeof(char)*(N1*2+1));
    temp[0]='\0';
    strcat(temp,S1);
    strcat(temp,S1);
    ptr=strstr(temp,S2);
    free(temp);
    if(ptr!=NULL)
       return 1;
    else
       return 0;
}
int main()
{
   char S1[10000],S2[10000];
   scanf("%s %s",S1,S2);
   if(arePalindrome(S1,S2))
      printf("Yes");
   else
      printf("No");
}
