/*
Author: Maahir Kalban
Assignment Number: Lab Assignment 1B
File Name: MaahirKalbanLab1B.zip
Course/Section: CS 2123 Section 31512
Due Date: 06/20/2020
Instructor: Bernard S. Ku
*/

/*Headers defines three variable types, several macros, and various functions for performing input and output.*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Recursive function declaration */
void reverse(char*, int, int);
//void reverse(char*);

/* Function to return string length */
//int string_length(char*);


int main()
{
    char chunk[255];                              //Initial character array for character string
    size_t len = sizeof(chunk);                   //Size of chunk array in bytes
    char *line = malloc(len);                     //Allocates the requested memory of size len
    FILE *fp = NULL;                              //File pointer to read from
    FILE *fpw = NULL;                             //File pointer to write to

    printf ("Processing..\n");                    //Notify user of status

    fp = fopen ("bible.txt", "r");                //Open and read file

    /*If file opened successfully, then read the string from file*/
      if(fp == NULL){
        perror("Unable to open file");
        return(-1);
    }

    /*Store the chunks of text in a line Buffer*/
     if(line == NULL){
        perror ("Unable to allocate memory for the line buffer.");
        return(-1);
     }

     line[0] = '\0';               //pt null character at the beginning of the line string to signal that the line is empty

    /*Get the entire file content from file pointer fp*/
    while(fgets(chunk,sizeof(chunk),fp)!=NULL){

    /*Resize the line buffer if necessary */
        if (len - strlen(line) < sizeof(chunk)){

            len *=2;                              //double size of line array

    /*Resize the memory block */
            if((line = realloc(line,len)) == NULL){
                perror("Unable to reallocate memory for the line buffer.");
                    free (line);
                    return (-1);
            }

        }
    /*Call Recursive function */
       reverse(chunk, 0, strlen(chunk)-1);

    /*Append the chunk to the end of the buffer*/
        strcat (line, chunk);                      //append chunk to line

    }


    /*Call Recursive function */
   // reverse(line, 0, strlen (line)-1);           /**Do not use: this returns memory dump**/


    /*Create, Open and Write to file pointer fpw */
    fpw =  fopen("reverseBible.txt", "w+");

    /* If file opened successfully, then write the string to file*/
    if ( fpw )
        {
        fputs(line,fpw);                            //put the reversed string in the reverseBible.txt file
        }
    else{
        printf("Failed to open the file\n");
        }

    fclose(fpw);                                    //close fpw file
    fpw = NULL;                                     //deallocate fpw pointer


    fclose(fp);                                    //close fp file
    fp = NULL;                                     //deallocate fp pointer
    free(line);                                    //free line string

    printf ("\nDone: reverseBible.txt is created\n\n");  //Notify user of status

     return 0;                                      //end main
}

/* Function to return reverse of the passed string */

void reverse(char *x, int begin, int end)
{
   char c;                                                //Character String passed from chunk

  /* Swapping first and last character*/
   if (begin >= end)
      return;

   c          = *(x+begin);                               //Character c assigned to from beginning
   *(x+begin) = *(x+end);                                 //First Character assigned to Last Character
   *(x+end)   = c;                                        //Last Character assigned c

   reverse(x, ++begin, --end);                            //Function calls reverse function (Thus Recursive function)
}
