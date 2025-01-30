#include <stdio.h>
void sort(int a[],int n)
{
    int i,j,temp;
    for (i=0;i<n-1;i++)
        for (j=0;j<n-i-1;j++)
            if (a[j]<a[j+1])
            {
                temp=a[j];
                a[j]=a[j+1];
                a[j+1]=temp;
            }
}
int bSearch(int a[],int n,int k)
{
    int L=0,H=n-1,mid;
    while (L<=H)
    {
        mid=L+(H-L)/2;
        if (a[mid]==k)
            return mid;
        if (a[mid]<k)
            L=mid+1;
        else
            H=mid-1;
    }
    return -1;
}
int main()
{
    int i, n, k, rst;
    printf("Enter the length of the array:");
    scanf("%d",&n);
    int b[n];
    printf("Enter the elements of the array:");
    for (i=0;i<n;i++)
        scanf("%d",&b[i]);
    sort(b,n);
    printf("Sorted array elements are:");
    for (i=0;i<n;i++)
        printf("%d ",b[i]);
    printf("\nEnter the search element:");
    scanf("%d",&k);
    rst = bSearch(b,n,k);
    if (rst==-1)
        printf("Element %d is not found.\n",k);
    else
        printf("Element %d is found at position %d.\n",k,rst+1);
    return 0;
}


