/*
Author: Maahir Kalban
Assignment Number: Assignment
File Name: wordProcessorLL.h
Course/Section: CS 5463-002
Due Date: 09/09/2020
Instructor: Dakai Zhu
*/
#ifndef _wordsProcessorLL_h
#define _wordsProcessorLL_h



typedef struct s_words {
    char *str;                  //word
    int count;                  //number of times word occurs
    struct s_words *next;       //pointer to next word
} words;


 words *create_words (char *word);
 words *add_word (words **wordList, char *word);
#endif
