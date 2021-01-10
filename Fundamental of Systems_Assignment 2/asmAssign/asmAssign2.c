/*
Author: Maahir Kalban
Assignment Number: Assignment 2 part 2
File Name: Kalban-Maahir-eart547-assignment2
Course/Section: CS 5463-002
Due Date: 09/17/2020
Instructor: Dakai Zhu
*/

/** C program to demonstrate Swap and Sum Functions **/

#include <stdio.h>
#include <stdlib.h>
#include "asmMagicSum.h"
#include "asmMagicSwap.h"

int main()
{
   int a = 1, b = 10; //Initialize variables for cSwap
   int num1 = 5, num2 = 6, num3; //Initialize variables for cSum

   printf("Before Swap. a: %d, b: %d\n", a, b);
   //Calling the cSwap function
   magicSwap(&a, &b);
   printf("After Swap of modified values. a: %d, b: %d\n\n", a, b);


   printf("Numbers to sum are: %d and %d\n", num1,num2);
   //Calling the cSum function
   num3 = magicSum(num1, num2);
   printf("Sum of (num1*2 + num2/2) is: %d\n", num3);

   return 0;
}
