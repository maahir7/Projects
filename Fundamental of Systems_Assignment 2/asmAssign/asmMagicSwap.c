/*
Author: Maahir Kalban
Assignment Number: Assignment 2 part 2
File Name: Kalban-Maahir-eart547-assignment2
Course/Section: CS 5463-002
Due Date: 09/17/2020
Instructor: Dakai Zhu
*/

#include <stdlib.h>
#include "asmMagicSwap.h"

void magicSwap(int *p1, int *p2) {
   int t0 = *p1 + 1;
   int t1 = *p2 - 1;
   *p1 = t1;
   *p2 = t0;
}
