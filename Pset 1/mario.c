#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        // ask user for size
        n = get_int("Size: ");
    }
    while (n < 1 || n > 8);

    for (int i = n; i > 0; i--)
    {
        //
        for (int j = 1; j < i; j++)
        {
            printf(" ");
        }
        for (int k = -1; k < n - i; k++)
        {
            printf("#");
        }
        //
        printf("\n");
    }
}
