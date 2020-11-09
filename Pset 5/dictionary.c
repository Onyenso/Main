// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdlib.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

node * create(char *s);
node * insert(node *head, char *s);
bool find(const char *s);


// Number of buckets in hash table
const unsigned int N = 65536;

// Hash table
node *table[N];

unsigned int words = 0;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    if (find(word))
    {
        return true;
    }
    return false;
}


// Hashes word to a number
unsigned int hash(const char *word)
{
    //unsigned int hashcode = (int) word[0] - 97;
    //return hashcode;
    unsigned int hash_value = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        hash_value = (hash_value << 2) ^ (int) word[i];
    }
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *dfile = fopen(dictionary, "r");
    if (dfile == NULL || ferror(dfile))
    {
        return false;
    }
    char dic_word[LENGTH + 1];
    while (fscanf(dfile, "%s", dic_word) != EOF)
    {
        unsigned int i = hash(dic_word);
        table[i] = insert(table[i], dic_word);
        words++;
        if (insert(table[i], dic_word) == NULL)
        {
            return false;
        }
    }
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return words;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}



bool find(const char *s)
{

    char dword[strlen(s) + 1];
    strcpy(dword, s);

    for (int j = 0; j < strlen(dword); j++)
    {
        dword[j] = tolower(dword[j]);
    }

    int i = hash(dword);

    for(node *tmp = table[i]; tmp != NULL; tmp = tmp->next)
    {
        if(strcmp(tmp->word, dword) == 0)
        {
            return true;
        }
    }
    return false;
}




node * create(char *s)
{
    node *new_node = malloc(sizeof(node));

    if(new_node == NULL)
    {
        return NULL;
    }
    strcpy(new_node->word, s);
    //new_node->word = s;
    new_node->next = NULL;
    return new_node;
}


node * insert(node *head, char *s)
{
    node *new_node = malloc(sizeof(node));
    if(new_node == NULL)
    {
        return NULL;
    }
    strcpy(new_node->word, s);
    new_node->next = head;
    head = new_node;
    return head;
}
