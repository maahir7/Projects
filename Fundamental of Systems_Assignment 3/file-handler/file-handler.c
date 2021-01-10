/*
Author: Maahir Kalban
Assignment Number: Assignment
File Name: file-handler
Course/Section: CS 5463-002
Due Date: 11/13/2020
Instructor: Dakai Zhu
*/

/** C program to simultaneously handle multiple input text files by creating multiple process (where each process is responsible to handle one input
file). Here, for each process, it will need to find out the number of words in its text file. Specifically, the process
will open the text file and parse through its content. It will count the total number words in the file. The typical
format to run the program with multiple input files is as follows: **/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include "wordsProcessorLL.h"


int main (int argc, char *argv[]) {

    words *mywords;             //head of linked list containing words
    mywords = NULL;
    char *delim = ". ,:;\t\n";

    FILE *myOutput = NULL;

  FILE *file[32];
  if (argc > 33) return 1;
  for (int i = 1; i < argc; ++i) {
    file[i-1] = fopen(argv[i], "r");  /* r for read */


      /*If file opened successfully, then read the string from file*/
      if(file[i-1] == NULL){
        perror("Unable to open file");
        return(-1);
    }

     pid_t pid = fork();

    if (pid < 0){
        perror ("Fork Failed");
    }
    if (pid ==0){


             int ch = 0, word = 1, k = 0;
    char thisword[100];
    while ((ch = fgetc (file[i-1])) != EOF) {  /* for each char    */
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


    myOutput = fopen ("output.txt", "w+");        //first parameter is input file

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

    }
  }

    return 0;
}

