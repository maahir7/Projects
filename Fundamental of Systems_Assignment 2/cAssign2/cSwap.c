/*
Author: Maahir Kalban
Assignment Number: Assignment 2 part 1
File Name: Kalban-Maahir-eart547-assignment2
Course/Section: CS 5463-002
Due Date: 09/17/2020
Instructor: Dakai Zhu
*/

#include <stdlib.h>
#include "cSwap.h"

void cSwap(int *i, int *j) {
   int t0 = *i;
   int t1 = *j;
   *i = t1;
   *j = t0;
}
