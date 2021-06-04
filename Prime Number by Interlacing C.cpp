#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>

int isPrime(long long int n){
   //# Checking for cases of 2 and 3
   if (n <= 1)	return 0;
   if (n <= 3)	return 1;
   //# skip checking middle five numbers in the loop
   if (n % 2 == 0 or n % 3 == 0)	return 0;
   long long int i = 5;
   while (i * i <= n){
      if (n % i == 0 || n % (i + 2) == 0){
         return 0;}
      i = i + 6;
  }
   return 1;
}
int main(){
	
	char n1[1001],n2[1001],n3[1001];
	scanf("%s %s",n1,n2);
	int s1=strlen(n1),s2=strlen(n2);
	if (s1==s2){
		int i=0,j=0;
		for(int k=0;k<s2;k++)	{
		n3[i++]=n1[k];n3[i++]=n2[k];
		n3[i]='\0';
	}
	}
	if(s1<s2){
		int i=0,j=0;
		for(int in=0;in<s1;++in){
			n3[i++]=n1[in];n3[i++]=n2[in];
		}
		int rem=abs(s2-s1);
		for(int in=rem;in<=s2+1;++in)	{n3[i++]=n2[in];}
		n3[i]='\0';
	}
	if(s1>s2){
		int i=0;
		for(int in=0;in<s2;++in){
			n3[i++]=n1[in];n3[i++]=n2[in];
		}
		int rem=abs(s1-s2);
		for(int in=rem;in<=s1+1;++in){n3[i++]=n1[in];}
		n3[i]='\0';
		
	}
	
	if (isPrime(atoi(n3)))	printf("%d and %d Interlaced is %d is a Prime Number",atoi(n1),atoi(n2),atoi(n3));
	else	printf("%d and %d Interlaced is %d is Not a Prime Number",atoi(n1),atoi(n2),atoi(n3));

	
}
