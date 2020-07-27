/*
Author:
Assignment Number: Lab Assignment 3
File Name: BST.h
Course/Section: CS 2123 Section 00x
Due Date:
Instructor: Dr. Ku
*/
#ifndef _BST_H
#define _BST_H

//structure for the tree nodes
typedef struct nodeT{
    struct nodeT *pLeft, *pRight;
    int value;
}nodeT;

//prototypes
nodeT* insert(nodeT *p, int x);
nodeT* newNodeT(int x);
void printTree(nodeT *p, int space);
void printInOrder(nodeT *p);
void report(nodeT *p);
nodeT* deleteNode(nodeT *pRoot, int value);
nodeT *minValueNode(nodeT *p);
nodeT* build(int left, int mid, int right);

int getHeight (struct nodeT* pRoot);
int getNumberOfNodes(struct nodeT *pRoot);
int getNumberOfLeaves(struct nodeT* pRoot);
void preorder(struct nodeT* pRoot);
void postorder(struct nodeT* pRoot);
_Bool contains(nodeT* pRoot, int key);

#endif
