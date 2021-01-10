/*
Author: Maahir Kalban
Assignment Number: Assignment
File Name: wordCount
Course/Section: CS 5463-002
Due Date: 09/09/2020
Instructor: Dakai Zhu
*/

/** C program to find out the number of words and how many times each word appears in a text file.
The program will open the text file and process its content.
It will find all different words and count the number of time each word appears in the file **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "wordsProcessorLL.h"


int main (int argc, char *argv[]) {

    words *mywords;             //head of linked list containing words
    mywords = NULL;
    char *delim = ". ,:;\t\n";

    FILE *myFile = NULL ;
    FILE *myOutput = NULL;


    myFile = fopen ("assign-01-test-input.txt", "r");     //first parameter is input file

    /*If file opened successfully, then read the string from file*/
      if(myFile == NULL){
        perror("Unable to open file");
        return(-1);
    }

    //start reading file character by character.
    //when word has been detected; call the add_word function

    int ch = 0, word = 1, k = 0;
    char thisword[100];
    while ((ch = fgetc (myFile)) != EOF) {  /* for each char    */
        if (strchr (delim, ch)) {           /* check if delim   */
            if (word == 1) {    /* if so, terminate word, reset */
                word = 0;
                thisword[k] = '\0';

                printf ("\nadd_word (mywords, %s)\n", thisword);
                /* do NOT overwrite list address each time,
                 * you must send ADDRESS of list to add_word
                 * to handle EMPTY list case.
                 */
                if (add_word (&mywords, thisword))
                  printf (" added: %s\n", mywords->str);

                else
                    fprintf (stderr, "error: add_word failed.\n");

                k = 0;
            }
        }
        else {  /* if not delim, add char to string, set word 1 */
            word = 1;
            thisword[k++] = tolower (ch);   /* make ch lowercase */
        }
    }
    if (word == 1) {    /* handle non-POSIX line-end */
        thisword[k] = '\0';

        //add thisword into the list
        printf ("\n add_word (mywords, %s) (last)\n", thisword);
        if (add_word (&mywords, thisword))  /* same comment as above */
            printf (" added: %s\n", mywords->str);
        else
            fprintf (stderr, "error: add_word failed.\n");
    }

    words *currword;
    printf ("printing list\n");


    //Traverse list and print each word and its count to outputfile
    //output file is second parameter being passed

    myOutput = fopen ("assign-01-test-output.txt", "w+");        //first parameter is input file

if (myOutput) {
    currword = mywords;

    while (currword != NULL) {  /* test currword here */

        //add word name then word count to file, then move to next
        fprintf (myOutput, "%s %d \n", currword->str, currword->count);
        printf ("%s ", currword->str);
        currword = currword->next;
    }
}
 else{
        printf("Failed to open the file\n");
        }
    putchar ('\n');
    return 0;
}

