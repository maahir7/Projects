/*
Author: Maahir Kalban
Assignment Number: Lab Assignment 4
File Name: MaahirKalbanLab4
Course/Section: CS 2123 Section 31512
Due Date: 07/25/2020
Instructor: Bernard S. Ku
*/

#include <stdio.h>
#include <stdlib.h>
//#include <stdbool.h>
#include <math.h>
#include "BST.h"



/**
 *Program to
 *Insert new items to BST, reports after each deletion
 *Check if the given node exists in BST
 *Delete items from BST, reports after each deletion
 **/

int main(int argc, char** argv) {
    nodeT *pRoot = NULL;        //root
    int data;                   //holds the int data

    printf("Construct an empty BST\n\n");
    report(pRoot);

    printf("\nThe height is = %d\n\n",getHeight(pRoot));
    printf("Number of nodes is = %d\n\n",getNumberOfNodes(pRoot));
    printf("Number of leaves is = %d\n\n",getNumberOfLeaves(pRoot));

    printf("\nNow insert a bunch of integers into the BST\n\n");
    printf("Try items not in the BST and some that are in it:\n\n");


    //Insertion of new items to BST, reports when done
    printf("Items to insert (-999 to stop): ");
    scanf("%d", &data);
    pRoot = insert(pRoot, data);
    printf("\nThe height is = %d\n\n",getHeight(pRoot));
    printf("Number of nodes is = %d\n\n",getNumberOfNodes(pRoot));
    printf("Number of leaves is = %d\n\n",getNumberOfLeaves(pRoot));


    while(data != -999){
    pRoot = insert(pRoot, data);
    printf("Items to insert (-999 to stop): ");
    scanf("%d", &data);
        if (contains(pRoot, data)){
            printf("\nThe number has existed!\n\n");
        }
        else{

    printf("\nThe height is = %d\n\n",getHeight(pRoot));
    printf("Number of nodes is = %d\n\n",getNumberOfNodes(pRoot));
    printf("Number of leaves is = %d\n\n",getNumberOfLeaves(pRoot));
        }
    }
    report(pRoot);


    //Check if the given node exists in it
    printf("\nNow testing the contains() operation.\n\n");
    printf("Try both items in the BST and some not in it:\n\n");
    printf("Item to Find (-999 to stop): ");
    scanf("%d", &data);

    if (contains(pRoot, data))
        printf("\nFound\n\n");
    else
        printf("\nNOT Found\n\n");

    while(data != -999){
    printf("Item to Find (-999 to stop): ");
    scanf("%d", &data);

    if (contains(pRoot, data))
        printf("\nFound\n\n");
    else
        printf("\nNOT Found\n\n");
    }


    //Deletion of items, reports after each deletion
    printf("\nNow testing the remove() operation\n\n");
    printf("Try both items in the BST and some not in it:\n");
    report(pRoot);

    printf("\nThe height is = %d\n\n",getHeight(pRoot));
    printf("Number of nodes is = %d\n\n",getNumberOfNodes(pRoot));
    printf("Number of leaves is = %d\n\n",getNumberOfLeaves(pRoot));


    printf("\nItem to remove (-999 to stop): ");
    scanf("%d", &data);
    while(data != -999){
        pRoot = deleteNode(pRoot, data);
        printf("\nThe height is = %d\n\n",getHeight(pRoot));
        printf("Number of nodes is = %d\n\n",getNumberOfNodes(pRoot));
        printf("Number of leaves is = %d\n\n",getNumberOfLeaves(pRoot));
        report(pRoot);
        printf("\nItem to remove (-999 to stop): ");
        scanf("%d", &data);
    }
    report(pRoot);

    return 0;
}


