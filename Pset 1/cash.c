#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)

{
    float dollars;
    //Prompt user for input
    do
    {
        dollars = get_float("Change owed: ");
    }
    //Reprompt if input is less than or equal to 0
    while (dollars <= 0);
    //Convert dollars to cents and round up
    int cents = round(dollars * 100);

    int firstremainder;
    int firstcoins;
    do
    {
        firstcoins = cents / 25;
        firstremainder = cents % 25;
    }
    while (firstremainder >= 25);
    //If there is no remainder after dividing by 25, do the following:
    if (firstremainder == 0)
    {
        printf("%i\n", firstcoins);
    }
    else if (firstremainder != 0)
    {

        int secondremainder;
        int i;
        int secondcoins;

        do
        {
            secondremainder = firstremainder % 10;
            i = firstremainder / 10;
            secondcoins = firstcoins + i;
        }
        while (secondremainder >= 10);
        //If there is no remainder after dividing by 10, do the following:
        if (secondremainder == 0)
        {
            printf("%i\n", secondcoins);
        }
        else if (secondremainder != 0)
        {
            int thirdremainder;
            int j;
            int thirdcoins;
            //
            do
            {
                thirdremainder = secondremainder % 5;
                j = secondremainder / 5;
                thirdcoins = secondcoins + j;
            }
            while (thirdremainder >= 5);
            //If there is no remainder after dividing by 5, do the following:
            if (thirdremainder == 0)
            {
                printf("%i\n", thirdcoins);
            }
            else
            {
                int fourthremainder;
                int k;
                int fourthcoins;
                //
                do
                {
                    fourthremainder = thirdremainder % 1;
                    k = thirdremainder / 1;
                    fourthcoins = thirdcoins + k;
                }
                //
                while (fourthremainder >= 1);
                printf("%i\n", fourthcoins);
            }
        }
    }
}
