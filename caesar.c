#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //Check if number of input arguments is 2
    if (argc != 2)
    {
        printf("User input error!!!\n");
        return 1;
    }
    //For each character of the string, do the following:
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        argv[i][i] = (unsigned char) argv[i][i];
        if (isdigit(argv[1][i]) == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    int key = atoi(argv[1]);
    //Get plaintext from user
    string s = get_string("plaintext: ");
    printf("ciphertext: ");
    //If key is greater than 26, use the value of its modulo function as new key
    if (key > 26)
    {
        key = key % 26;
    }
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        //In order to use "islower" function, cast each chaaracter to an unsigned char
        s[i] = (unsigned char) s[i];
        //If the character is a lower case letter
        if (islower(s[i]) != 0)
        {
            s[i] = s[i] + key;
            if (s[i] > 122 && s[i] <= 127)
            {
                s[i] = s[i] - 26;
            }
            else if (s[i] < 97)
            {
                s[i] = s[i] - 26;
            }
            printf("%c", s[i]);
        }
        //If the character is an uppercase letter
        else if (isupper(s[i]) != 0)
        {
            s[i] = s[i] + key;
            if (s[i] > 90 && s[i] < 97)
            {
                s[i] = s[i] - 26;
            }
            printf("%c", s[i]);
        }
        else
        {
            printf("%c", s[i]);
        }

    }
    printf("\n");
    return 0;
}
