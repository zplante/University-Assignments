//-----------------------------------------------------------------------------
//   IntegerLinkedList.c
//   Implementation file for IntegerLinkedList ADT
//-----------------------------------------------------------------------------
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>
#include"Dictionary.h"

// private types --------------------------------------------------------------

// NodeObj
typedef struct NodeObj{
    int item;
    struct NodeObj* next;
} NodeObj;

// Node
//see .h file for defn

// newNode()
// constructor of the Node type
Node newNode(int x) {
    Node N = malloc(sizeof(NodeObj));
    assert(N!=NULL);
    N->item = x;
    N->next = NULL;
    return(N);
}

// freeNode()
// destructor for the Node type
void freeNode(Node *pN){
    if( pN!=NULL && *pN!=NULL){
        free(*pN);
        *pN = NULL;
    }
}

// LinkedListObj
typedef struct DictionaryObj{
    Node top;
    int numItems;
} DictionaryObj;

// public functions -----------------------------------------------------------

// newLinkedList()
// constructor for the LinkedList type
Dictionary newDictionary(void){
    Dictionary S = malloc(sizeof(DictionaryObj));
    assert(S!=NULL);
    S->top = NULL;
    S->numItems = 0;
    return S;
}

// freeLinkedList()
// destructor for the LinkedList type
void freeDictionary(Dictionary* pS){
    if( pS!=NULL && *pS!=NULL)
    {
        Node N = (*pS)->top;
        Node temp;
        while(N != NULL)
        {
            temp = N->next;
            freeNode(&N);
            N = temp;
        }
        freeNode(&N);
        free(*pS);
        *pS = NULL;
    }
}

//-----------------------------------------------------------------------------
// definitions of ADT operations (only giving printLinkedList, you need to do the rest)
//-----------------------------------------------------------------------------

Node find(int number, Dictionary S)
{
    Node N;
    for(N=S->top; N!=NULL; N=N->next)
    {
        if(N->item == number)
        {
            return N;
        }
    }
    return NULL;
}

void addNode(Node N, Dictionary S)
{
    Node currentNode;
    if(S->top == NULL)
    {
        S->top = N;
    }
    else
    {
        currentNode = S->top;
        while(currentNode->next != NULL)
        {
            currentNode = currentNode->next;
        }
        currentNode->next = N;
    }
    S->numItems++;
}

void insert(int num, Dictionary S)
{
    Node N = newNode(num);
    Node currentNode;
    if(S->top == NULL)
    {
        S->top = N;
    }
    else
    {
        currentNode = S->top;
        while(currentNode->next != NULL)
        {
            currentNode = currentNode->next;
        }
        currentNode->next = N;
    }
    S->numItems++;
}

void printList(Dictionary S)
{
    Node temp = S->top;

    while(temp != NULL)
    {
        printf("%d,", temp->item);
        temp = temp->next;
    }
    printf("\n");
}

void delete(int n, Dictionary S)
{
    Node N;
	Node prev;
	for(N=S->top; N!=NULL; N=N->next) 
	{
		if(N->item == n)
		{
			if(N == S->top)
			{
				S->top = N->next;
			}
			else
			{
				prev->next = N->next;
			}
			freeNode(&N);
			break;
		}
		prev = N;
	}
}

// printLinkedList()
// prints a text representation of S to the file pointed to by out
// pre: none
void printDictionary(FILE* out, Dictionary S){
    Node N;
    if( S==NULL ){
        fprintf(stderr,
                "LinkedList Error: calling printLinkedList() on NULL LinkedList reference\n");
        exit(EXIT_FAILURE);
    }
    for(N=S->top; N!=NULL; N=N->next)
    {
        if(N->next != NULL)
        {
            fprintf(out, "%d -> ", N->item);
        }
        else
        {
            fprintf(out, "%d", N->item);
        }
    }
    fprintf(out, "\n");
}
