#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
//Zac Plante
//zplante
typedef struct IntVecNode {
    int * data;
    int sz;
    int capacity;
} IntVecNode;

/** intInitCap: initial capacity after intMakeEmptyVec() */
static const int intInitCap;


int intTop(IntVec myVec){
    if(myVec==NULL) {
        return EXIT_FAILURE;
    }
    return myVec->data[myVec->sz-1];
}


int intData(IntVec myVec, int i){
    if(myVec==NULL||i<0||i>myVec->sz-1){
        return EXIT_FAILURE;
    }
    return myVec->data[i];
}


int intSize(IntVec myVec){
    if(myVec==NULL){
        return EXIT_FAILURE;
    }
    return myVec->sz;
}
int intCapacity(IntVec myVec){
    if(myVec==NULL){
        return EXIT_FAILURE;
    }
    return myVec->capacity;
}


/** intMakeEmptyVec()
 * preconditions: none.
 * postconditions: Let /return be the value returned by intMakeEmptyVec().
 *    Then intCapacity(/return) == 4, intSize(/return) == 0).
 */
IntVec intMakeEmptyVec(void) {
    IntVec newVec;
    newVec = calloc(1,sizeof(struct IntVecNode));
    newVec->data = calloc(intInitCap, sizeof(int));
    newVec->sz = 0;
    newVec->capacity=intInitCap;
    return newVec;
}
/* Manipulation Procedures
 */

/** intVecPush()
 * precondition: myVec has been constructed.
 * postconditions: Let /sz/ = intSize(myVec) before the call.
 *                 Let /cap/ = intCapacity(myVec) before the call.
 *    Then after the call, intSize(myVec) == /sz/+1,
 *        and intTop(myVec) == newE and intData(myVec, /sz/) == newE.
 *    Also, for all 0 <= i < /sz/: intData(myVec, i) is unchanged.
 *    Also, if (/sz/+1) > /cap/, then after the call,
 *        intCapacity(myVec) = 2 * /cap/.
 *    otherwise, intCapacity(myVec) is unchanged.
 */
void intVecPush(IntVec myVec, int newE){
    if(myVec->sz==myVec->capacity){
        int newCap;
        newCap=2*myVec->capacity;
        int* newData;
        newData=realloc(myVec->data,newCap*sizeof(int));
        if(newData != myVec->data){
            myVec->data=newData;
        }
        myVec->capacity =newCap;
    }
    myVec->data[myVec->sz]=newE;
    myVec->sz=myVec->sz+1;
}
void intVecPop(IntVec myVec){
    if(myVec->sz!=0) {
        myVec->sz = myVec->sz - 1;
    }
}





