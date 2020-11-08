#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = get_int("Height: ");

    int counter = 1;

    for (int i = 0; i < height; i++)
    {
        for (int n = counter; n <= height; n+=counter)
        {
            for (int j = height - counter; j > 0; j--)
            {
                printf(" ");
            }
            for (int k = 0; k < counter; k++)
            {
                printf("#");
            }
            printf("\n");
            counter++;
        }
    }
}

