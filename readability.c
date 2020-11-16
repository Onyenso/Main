#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    //Prompt user for text
    string text = get_string("Text: ");

    //Declare variables
    int letterscount = 0, wordscount = 1, sentencecount = 0, index;
    double lettersper100, sentenceper100;

    for (int i = 0, n = strlen(text); i < n; i++)
        //For ith character(text[i]) of the string, do the following:
    {
        text[i] = (unsigned char) text[i];

        if (isalpha(text[i]) != 0)
        {
            letterscount++;
        }
        else if (isspace(text[i]) != 0)
        {
            wordscount++;
        }
        else if (text[i] == 46 || text[i] == 33 || text[i] == 63)
        {
            sentencecount++;
        }
    }
    //Find the average number of letters and sentences per 100 words
    lettersper100 = (letterscount * 100) / (double)wordscount;
    sentenceper100 = (sentencecount * 100) / (double)wordscount;

    //Use Coleman-Liau formula to find the grade
    index = round(0.0588 * lettersper100 - 0.296 * sentenceper100 - 15.8);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

