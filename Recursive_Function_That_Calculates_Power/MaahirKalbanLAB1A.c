/*
Author: Maahir Kalban
Assignment Number: Lab Assignment 1A
File Name: MaahirKalbanLab1A.zip
Course/Section: CS 2123 Section 31512
Due Date: 06/20/2020
Instructor: Bernard S. Ku
*/

#include <stdio.h>


/* Power function declaration */
double power(double a, int n);


int main()
{
    double a, power1;                   // initialize double for base and power
    int n;                              // initialize int for n

    /* Input base and exponent from user */
    printf("Enter base: ");
    scanf("%lf", &a);
    printf("Enter exponent: ");
    scanf("%d", &n);

    /* Call power function*/
    power1 = power(a, n);

    printf("%.0lf raised to %d = %f", a, n, power1);   //print the results

    return 0;                                          //end main
}


/*
 * Calculate power of any number using recursive function
 * Returns a^n
 */
double power(double a, int n)
{
    /* Base condition */
    if(n == 0)                          //for n = 0
        return 1;                       //Base case
    else if(n > 0)                      //for n > 0
        return a * power(a, n - 1);     //Function calling power function(Recursive Function)
    else                                //for n < 0
        return 1 / power(a, -n);        //Function calling power function(Recursive Function)
}
