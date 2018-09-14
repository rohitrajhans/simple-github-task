#include<stdio.h>
#include<math.h>

void main()
{
  int n,i,a;
  printf("Enter your number");
  scanf("%d",&n);
  a=sqrt(n);

  for(i=2;i<=a;i++)
  if(n%i==0)
  break;

  if(i==a+1)
  printf("%d is a prime number",n);
  else
  printf("%d is not a prime number",n);
  getch();
}
