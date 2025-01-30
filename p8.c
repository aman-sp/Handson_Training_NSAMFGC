#include <stdio.h>
int search(int a[],int n,int k)
{
    int i;
    for(i=0;i<n;i++)
        if(k==a[i])
            return i;
    return -1;
}
int main()
{
    int i,n,j,k,f=0,rst;
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
    rst=search(a,n,k);
    if(rst==-1)
        printf("Element %d is not found.",k);
    else
        printf("Element %d is found in %d Position.",k,rst+1);
    return 0;
}
