//-----------------------------------------------------------------------------
// IntegerLinkedList.h
// Header file for the IntegerLinkedList ADT
//-----------------------------------------------------------------------------

#ifndef _DICTIONARY_H_INCLUDE_
#define _DICTIONARY_H_INCLUDE_

#include<stdio.h>

// LinkedList
// Exported reference type
typedef struct DictionaryObj* Dictionary;

// Node
// Exported reference type
typedef struct NodeObj* Node;

//constructor for node
Node newNode(int x);

// newLinkedList()
// constructor for the LinkedList type
Dictionary newDictionary(void);

// freeLinkedList()
// destructor for the LinkedList type
void freeDictionary(Dictionary* pS);

//-----------------------------------------------------------------------------
// prototypes of ADT operations deleted to save space, see webpage
//-----------------------------------------------------------------------------

void addNode(Node N, Dictionary S);

void printList(Dictionary S);


// printLinkedList()
// prints a text representation of S to the file pointed to by out
// pre: none
void printDictionary(FILE* out, Dictionary S);

// insert()
// insert number into linked list
// pre: none
void insert(int number, Dictionary S);

// find()
// find pointer to node containing number (read next code snippet for details), return //      null if none exists
// pre: none
Node find(int number, Dictionary S);

// delete()
// delete number from linked list
// pre: none
void delete(int n, Dictionary S);

#endif
