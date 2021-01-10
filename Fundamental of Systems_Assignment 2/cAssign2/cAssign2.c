/*
Author: Maahir Kalban
Assignment Number: Assignment 2 part 1
File Name: Kalban-Maahir-eart547-assignment2
Course/Section: CS 5463-002
Due Date: 09/17/2020
Instructor: Dakai Zhu
*/

/** C program to demonstrate Swap and Sum Functions **/

#include <stdio.h>
#include <stdlib.h>
#include "cSwap.h"
#include "cSum.h"

int main()
{
   int a = 3, b = 4; //Initialize variables for cSwap
   int num1 = 10, num2 = 20, num3; //Initialize variables for cSum

   printf("Before Swap. a: %d, b: %d\n", a, b);
   //Calling the cSwap function
   cSwap(&a, &b);
   printf("After Swap. a: %d, b: %d\n\n", a, b);


   printf("Numbers to sum are: %d and %d\n", num1,num2);
   //Calling the cSum function
   num3 = cSum(num1, num2);
   printf("Sum of the Numbers is: %d\n", num3);

   return 0;
}
