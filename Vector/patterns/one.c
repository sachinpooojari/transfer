#include<stdio.h>
main()
{
	int i,j,n,k;
	scanf("%d",&n);
	
		for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{	
			printf(" ");
			
		}
		for(k=n;k>i;k--)
		{
			printf("v");
		}
		printf("\n");
	}
}
