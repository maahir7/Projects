/*
Author: Maahir Kalban
Assignment Number: Assignment
File Name: wordProcessorLL.c
Course/Section: CS 5463-002
Due Date: 09/09/2020
Instructor: Dakai Zhu
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "wordsProcessorLL.h"

 words *create_words (char *word)
{
    //allocate space for the structure
    printf ("%lu ", strlen (word));
    words *newWord = malloc (sizeof (words));
    if (NULL != newWord) {

        //allocate space for storing the new word in "str"
        newWord->str = (char *) malloc ((strlen (word)) + 1);
        strcpy (newWord->str, word);    //copy “word” into newWord->str
        newWord->str[strlen (word)] = '\0';
        printf (" Create: %s ", newWord->str);
        //initialize count to 1;
        newWord->count = 1;
        //initialize next;
        newWord->next = NULL;
    }
    return newWord;
}

 words *add_word (words **wordList, char *word)
{
    if (!*wordList) {       /* handle EMPTY list */
        printf ("NEW LIST\n");
        return *wordList = create_words (word);
    }

    words *temp = *wordList;
    // search if word exists in the list; if so, make found=1
    while (temp->next != NULL) {    /* iterate while temp->next != NULL */

        if (strcmp (temp->str, word) == 0) {    //use strcmp command
            temp->count = temp->count + 1;      //increment count;
            return *wordList;
        }
        else
            temp = temp->next;  //update temp
    }
    words *newWord = create_words (word);
    if (NULL != newWord) {  /* insert at TAIL of list */
        temp->next = newWord;
        printf (" NEW WORD: %s\n ", newWord->str);
    }
    return newWord;
}
