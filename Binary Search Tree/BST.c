/*
Author:
Assignment Number: Lab Assignment 3
File Name: BST.c
Course/Section: CS 2123 Section 00x
Due Date:
Instructor: Dr. Ku
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "BST.h"


/******************** deleteNode **************************************
Purpose:
 * Deletes a node from a binary tree, replacing it with the node that has the
 * smallest value that is greater than the value of the deleted node.
Parameters:
 * I    nodeT *pRoot    the root of the tree
 * I    int value       the value that needs deleting
Returns:
 * The head of the tree that now has the node deleted. If the value is not in
 * the tree, it will print an error message and return the root.
Notes:
 * Recursive. Uses minValueNode().
**************************************************************************/
nodeT* deleteNode(nodeT *pRoot, int value){
    // base case
    if (pRoot == NULL) {
        printf("\n-----error--------\n");
        printf("\nDid not find this item!\n");
        printf("\nThe number not in the tree!\n");
        return pRoot;
    }

    // If the value to be deleted is smaller than the pRoot's value,
    // then it lies in left subtree
    if (value < pRoot->value)
        pRoot->pLeft = deleteNode(pRoot->pLeft, value);

    // If the value to be deleted is greater than the pRoot's value,
    // then it lies in right subtree
    else if (value > pRoot->value)
        pRoot->pRight = deleteNode(pRoot->pRight, value);

    // if value is same as pRoot's value, then This is the node
    // to be deleted
    else
    { // node with only one child or no child
        if (pRoot->pLeft == NULL)
        {
            nodeT *temp = pRoot->pRight;
            free(pRoot);
            return temp;
        }
        else if (pRoot->pRight == NULL)
        {
            nodeT *temp = pRoot->pLeft;
            free(pRoot);
            return temp;
        }

        // node with two children: Get the inorder successor (smallest
        // in the right subtree)
        nodeT *temp = minValueNode(pRoot->pRight);

        // Copy the inorder successor's content to this node
        pRoot->value = temp->value;

        // Delete the inorder successor
        pRoot->pRight = deleteNode(pRoot->pRight, temp->value);
    }
    return pRoot;
}

/******************** minValueNode **************************************
Purpose:
 * Finds the smallest value in a tree.
Parameters:
 * I    nodeT *p    the root of the tree
Returns:
 * A pointer to the smallest value in the tree.
Notes:
 * Recursive. If given an empty tree it will display an error message and return
 * the NULL pointer.
**************************************************************************/
nodeT *minValueNode(nodeT *p){
    //if given a null pointer
    if(p==NULL){
        printf("Error");
        return p;
    }
    //returns p when it is the smallest value
    if(p->pLeft==NULL)
        return p;
    minValueNode(p->pLeft);
}


/******************** printTree **************************************
Purpose:
 * Prints the input tree in a horizontal hierarchy.
Parameters:
 * I    nodeT *p    the root of the tree
 * I    int space   Used for spacing of the tree levels
Returns:
 * N/A
Notes:
 * Recursive. If given an empty tree it will do nothing.
**************************************************************************/
void printTree(nodeT *p, int space){
    int i;          //iterator

    //if given an empty tree
    if (p == NULL)
        return;

    space += 5; //increases space between levels

    //processes right side first
    printTree(p->pRight, space);
    printf("\n");

    //where the printing actually happens
    //i starts at 5 so the root is flush with the edge of the screen
    for (i = 5; i < space; i++)
        printf(" ");
    printf("%d\n", p->value);

    //processes left side
    printTree(p->pLeft, space);
}

/******************** printInOrder **************************************
Purpose:
 * Prints the tree's values in order
Parameters:
 * I    nodeT *p    the root of the tree
Returns:
 * N/A
Notes:
 * Recursive. If given an empty tree it will do nothing.
**************************************************************************/
void printInOrder(nodeT *p){
    if(p == NULL)
        return;
    printInOrder(p->pLeft);
    printf("%d ", p->value);
    printInOrder(p->pRight);
}



/******************** report **************************************
Purpose:
 * Displays all information on the Binary tree
Parameters:
 * I    nodeT *p    the root of the tree
Returns:
 * N/A
Notes:
 * Recursive. If given an empty tree it will do nothing. Uses getHeight(),
 * getNumberOfNodes(), getNumberofLeaves(), printTree(), printInOrder(),
 * printPreOrder(), and printPostOrder().
**************************************************************************/
void report(nodeT *p){
    //if given an empty tree
    if (p == NULL){
        printf("\nBST is empty!\n");
        return;
    }
        else{
            printTree(p, 0);
            printf("\nBST is not empty\n");
            printf("\nInorder Traversal of BST: \n");
            printInOrder(p);
            printf("\n");
            printf("\nPreorder Traversal of BST:\n");
            preorder(p);
            printf("\n");
            printf("\nPostorder Traversal of BST:\n");
            postorder(p);
            printf("\n");
        }
}

/******************** insert **************************************
Purpose:
 * Inserts Values into a binary tree
Parameters:
 * I    nodeT *p    the root of the tree
 * I    int x       the value to insert
Returns:
 * the root of the tree (pointer).
Notes:
 * Recursive.
**************************************************************************/
nodeT* insert(nodeT *p, int x){
    //If tree is empty or if reached the end of a branch, creates a nodeT
    //and and inserts it
    if(p==NULL){
        return newNodeT(x);
    }
    //if x already exists, it returns a pointer to it.
    //This does not create a new node or overwrite the old one
    if(x == p->value)
        return p;
    //if x is less than p's value, it will overwrite
    //pLeft with the return of the recursion moving left
    else if(x < p->value)
        p->pLeft = insert(p->pLeft, x);
    //if x is greater than p's value, it will overwrite
    //pRight with the return of the recursion moving right
    else
        p->pRight = insert(p->pRight, x);
    //returns p. At end of recursion this will be the pRoot.
    return p;
}

/******************** newNodeT **************************************
Purpose:
 * Creates a new nodeT with initialized values
Parameters:
 * I    int x       the value fro the node
Returns:
 * Pointer to the newly created nodeT
Notes:
 * Recursive.
**************************************************************************/
nodeT* newNodeT(int x){
    //creates a new node
    nodeT *pNew = (nodeT *) malloc(sizeof(nodeT));
    //Prints error if there is a problem with the memory allocation
    if (pNew == NULL){
        printf("Memory allocation error");
        return NULL;
    }
    //initializes the values
    pNew->value = x;
    pNew->pLeft = NULL;
    pNew->pRight = NULL;
    //returns newly created node
    return pNew;
}


nodeT* build(int left, int mid, int right){
    if(left==mid||mid==right)
        return NULL;
    nodeT *pRoot = newNodeT(mid);
    pRoot->pLeft= build(left, ceil((left+mid)/2), mid);
    pRoot->pRight= build(mid, (mid+right)/2, right);
    return pRoot;
}

// Function to get BST height//
int getHeight(struct nodeT* pRoot)
{
   if (pRoot==NULL)
       return -1;
   else
   {
       /* compute the depth of each subtree */
       int lDepth = getHeight(pRoot->pLeft);
       int rDepth = getHeight(pRoot->pRight);

       /* use the larger one */
       if (lDepth > rDepth)
           return(lDepth+1);
       else return(rDepth+1);
   }
}

// Function to get number of nodes in BST//
int getNumberOfNodes(struct nodeT *pRoot){
   if(pRoot==NULL){
       return(0);
   }
   else{
       /* increment height */
       return(1+getNumberOfNodes(pRoot->pLeft)+getNumberOfNodes(pRoot->pRight));
   }
}

// Function to get number of leaves in BST//
int getNumberOfLeaves(struct nodeT* pRoot)
{
  if(pRoot == NULL)
    return 0;
  if(pRoot->pLeft == NULL && pRoot->pRight==NULL)
    return 1;
  else
    return getNumberOfLeaves(pRoot->pLeft)+
           getNumberOfLeaves(pRoot->pRight);
}

// Function to pre order tree traversals//
void preorder(struct nodeT* pRoot){
   if(pRoot==NULL){
       return;
   }
   else{
       printf("%d ",pRoot->value);
       preorder(pRoot->pLeft);
       preorder(pRoot->pRight);
   }
}


// Function to post order tree traversals//
void postorder(struct nodeT* pRoot){
   if(pRoot==NULL){
       return;
   }
   else{
       postorder(pRoot->pLeft);
       postorder(pRoot->pRight);
       printf("%d ",pRoot->value);
   }
}
// Function to traverse the tree in preorder and check if the given node exists in it
_Bool contains(nodeT* pRoot, int key)
{

    if (pRoot == NULL)
        return false;

    else if (pRoot->value == key)
        return true;

    /* then recur on left subtree */
    bool res1 = contains(pRoot->pLeft, key);

    if(res1) return true; // node found, no need to look further

    /* node is not found in left, so recur on right subtree */
    bool res2 = contains(pRoot->pRight, key);

    return res2;
}




