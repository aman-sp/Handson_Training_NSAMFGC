#include <stdio.h>
void main()
{
    int i,n,j,k,f=0;
    printf("Enter the length of the array:");
    scanf("%d",&n);
    int a[n];
    printf("Enter the elements of the array:");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the search element:");
    scanf("%d",&k);
    for(i=0;i<n;i++)
    {
        if(k==a[i])
        {
            printf("Element %d is found in %d Position.",k,i+1);
            break;
        }
    }
    printf("Element %d is not found.",k);
}
