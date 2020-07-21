/*
Author: Maahir Kalban
Assignment Number: Lab Assignment 3
File Name: MaahirKalbanLab3
Course/Section: CS 2123 Section 31512
Due Date: 07/20/2020
Instructor: Bernard S. Ku
*/

/* C program to evaluate value of a postfix expression from the user,
postfix expression form text file and convert infix to postfix form text file*/

#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
#include "stackar.h"   // For user input stack
#include "stackar2.h" // For postfix.txt and infix.txt conversion stack

int evaluatePostfix(char* exp);                     // To evaluate postfix
bool isOperator(char ch);                           // Check operator
int performOperation (int op1, int op2, char op);   // Perform calculation
int infixToPostfix(char* exp);                      // Convert infix to postfix
int isOperand(char ch);                             // Check if operand is valid
int Precedence(char ch);                            // To determine precedence of operator


// Driver program
int main()
{

    char exp[100] = {0} ,exp1[100] = {0}, buffer[15] = {0};  // Initialize variables
    int i, op1, op2, j, x, len, choice;
    Stack S;                                                 // Initialize Stack
    S = CreateStack( 200 );                                  // Create Stack size 200
    FILE *fp = NULL;                                         // Initialize file pointer
    FILE *fp1 = NULL;

       printf ("Enter Valid PostFix Function to be Evaluated: (e.g. 2 3 + 4 * ) \n");
       scanf("%[^\n]%*c",exp1);
       len = strlen(exp1);


        j=0;

        for(i=0; i<len;i++){
            if (exp1[i]>='0' && exp1[i]<='9'){
                buffer[j++] = exp1[i];
                }
            else if (exp1[i]== ' '){
                if (j>0){
                    buffer[j] ='\0';
                    x  = atoi(buffer);
                    Push(x ,S);
                    j=0;
                }
            }
            else if (isOperator(exp1[i])){
                op1 = Top(S);
                Pop(S);
                op2 = Top(S);
                Pop(S);
                Push(performOperation(op1,op2,exp1[i]), S);
            }

        }

        printf ("\nPostfix evaluation: %d \n\n",Top(S));


                /*Menu*/
    while(1)
    {
        printf("\n\n\t\t Postfix Evaluation Menu\n\n");
        printf("\n1. Postfix Evaluation from 'postfix.txt':\n\n");
        printf("\n2. Infix to Postfix conversion from 'infix.txt':\n\n");
        printf("\n3. Exit\n\n");
        printf("\nEnter your choice (1, 2 , or 3) :  ");
        scanf("%d",&choice);

        switch(choice)
        {

            case 1:                                 //Evaluate Postfix from 'postfix.txt'
                fp = fopen("postfix.txt", "r");


                /*If file opened successfully, then read the string from file*/
                if(fp == NULL){
                perror("Unable to open file");
                return(-1);
                }

                exp[0] = '\0';               //pt null character at the beginning of the line string to signal that the line is empty

                while(fgets(exp,sizeof(exp),fp)!=NULL){

                printf ("\nPostFix Function: %s \n",exp);

                printf ("\nPostfix evaluation: %d\n",  evaluatePostfix(exp));

                }
                fclose(fp);
                fp = NULL;

                break;

            case 2:                                         //Evaluate infix to Postfix from 'infix.txt'

                fp1 = fopen("infix.txt", "r");


                /*If file opened successfully, then read the string from file*/
                if(fp1 == NULL){
                perror("Unable to open file");
                return(-1);
                }

                exp[0] = '\0';               //pt null character at the beginning of the line string to signal that the line is empty

                while(fgets(exp,sizeof(exp),fp1)!=NULL){

                printf ("\nInfix Function: %s \n",exp);

                infixToPostfix(exp);
                }

                fclose(fp1);
                fp1 = NULL;


                break;

            case 3:                                                     // End of Menu
                printf("\n\n\t\t\t End of Program! \n\n\n");
                exit(0);    // terminates the complete program execution
        }
    }


	return 0;
}

  // Function to Check operator
bool isOperator(char ch){
    if (ch == '+'|| ch == '-' || ch == '*' || ch == '/' )
        return true;
    else
        return false;
}

// Function to Perform calculation
int performOperation (int op1, int op2, char op){

int ans;
switch (op){
case '+':
    ans = op2 + op1;
    break;
case '-':
    ans = op2 - op1;
    break;
case '*':
    ans = op2 * op1;
    break;
case '/':
    ans = op2 / op1;
    break;
    }
    return ans;
}
// Function to Convert infix to postfix
int infixToPostfix(char* exp)
{
	int i, k;

	// Create a stack of capacity equal to expression size
	struct Stack* stack = createStack(strlen(exp));
	if(!stack) // See if stack was created successfully
		return -1 ;

	for (i = 0, k = -1; exp[i]; ++i)
	{
		// If the scanned character is an operand, add it to output.
		if (isOperand(exp[i]))
			exp[++k] = exp[i];

		// If the scanned character is an ‘(‘, push it to the stack.
		else if (exp[i] == '(')
			push(stack, exp[i]);

		// If the scanned character is an ‘)’, pop and output from the stack until an ‘(‘ is encountered.

        else if (exp[i] == ')')
		{
			while (!isEmpty(stack) && peek(stack) != '(')
				exp[++k] = pop(stack);
			if (!isEmpty(stack) && peek(stack) != '(')
				return -1; // invalid expression
			else
				pop(stack);
		}
		else // an operator is encountered
		{
			while (!isEmpty(stack) && Precedence(exp[i]) <= Precedence(peek(stack)))
				exp[++k] = pop(stack);
			push(stack, exp[i]);
		}

	}

	// pop all the operators from the stack
	while (!isEmpty(stack))
		exp[++k] = pop(stack );

	exp[++k] = '\0';
	printf( "\nThe PostFix Function is: %s\n", exp );
}

   // Check if operand is valid
int isOperand(char ch)
{
	return (ch >= '0' && ch <= '9');
}
  // To evaluate postfix
int evaluatePostfix(char* exp)
{
    // Create a stack of capacity equal to expression size
    struct Stack* stack = createStack(strlen(exp));
    int i;

    // See if stack was created successfully
    if (!stack) return -1;

    // Scan all characters one by one
    for (i = 0; exp[i]; ++i)
    {
        // If the scanned character is an operand (number here),
        // push it to the stack.
        if (isdigit(exp[i]))
            push(stack, exp[i] - '0');

        // If the scanned character is an operator, pop two
        // elements from stack apply the operator
        else
        {
            int val1 = pop(stack);
            int val2 = pop(stack);
            switch (exp[i])
            {
            case '+': push(stack, val2 + val1); break;
            case '-': push(stack, val2 - val1); break;
            case '*': push(stack, val2 * val1); break;
            case '/': push(stack, val2/val1); break;
            }
        }

    }

    return pop(stack);
}

//To determine precedence of operator
int Precedence(char ch)
{
	switch (ch)
	{
	case '+':
	case '-':
		return 1;

	case '*':
	case '/':
		return 2;
    }
	return -1;
}

