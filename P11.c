..
#include <stdio.h>
#include <stdlib.h>
int stack[100],top=-1,n,f=0;
void create()
{
    if (f==0)
    {
        printf("Enter the size of the stack: ");
        scanf("%d",&n);
        printf("Stack is created.\n");
        f++;
    }
    else
        printf("Stack is already created.\n");
}

void push()
{
    int value;
    if (top==n-1)
        printf("Stack overflow.\n");
    else
    {
        printf("Enter the value to be pushed: ");
        scanf("%d",&value);
        top++;
        stack[top]=value;
        printf("Value pushed.\n");
    }
}

void pop()
{
    if (top==-1)
        printf("Stack underflow.\n");
    else
    {
        printf("Value popped: %d\n", stack[top]);
        top--;
    }
}
/*
void rev()
{
    if(top==-1)
    {
        printf("Stack is empty.\n");
    }
    else
    {
        printf("Stack elements are: ");
        for (int i=top;i>=0;i--)
        {
            printf("%d ",stack[i]);
        }
        printf("\n");
    }
}
*/

void dsp()
{
    if(top==-1)
    {
        printf("Stack is empty.\n");
    }
    else
    {
        printf("Stack elements are: ");
        for (int i=top;i>=0;i--)
        {
            printf("%d ",stack[i]);
        }
        printf("\n");
    }
}

int main()
{
    int ch;
    while (1)
    {
        printf("\nEnter your choice:\n");
        printf("1.Create Stack\n");
        printf("2.Push\n");
        printf("3.Pop\n");
        printf("4.Display\n");
        printf("5.Exit\n");
        scanf("%d",&ch);
        switch (ch)
        {
            case 1:create();
                   break;
            case 2:push();
                   break;
            case 3:pop();
                   break;
            case 4:dsp();
                   break;
            case 5:exit(0);
            default:printf("Enter a valid choice.\n");
                    break;
        }
    }
    return 0;
}
