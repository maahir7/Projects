// from https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/
#ifndef _stackar2_h
#define _stackar2_h

struct Stack;
typedef struct Stack *stack;

struct Stack* createStack( unsigned capacity );
int isEmpty(struct Stack* stack);
char peek(struct Stack* stack);
char pop(struct Stack* stack);
void push(struct Stack* stack, char op);

        #endif  /* _Stack_h */

