#include <stdio.h>
int main() 
{
    char st[100];
    printf("Enter a string:");
    fgets(str,sizeof(str),stdin);
    for(int i=0;str[i]!='\0';i++)
    {    if(str[i]==' ')
            str[i]='\n';
    }
    printf("%s",str)
    return 0;
}