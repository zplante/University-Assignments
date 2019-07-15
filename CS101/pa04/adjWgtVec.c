//
// Created by Zac Plante on 6/5/17.
//
#include<stdio.h>
#include<stdlib.h>
#include "adjWgtVec.h"

typedef struct AdjWgtVecNode {
    AdjWgt * data;
    int sz;
    int capacity;
} AdjWgtVecNode;



AdjWgt adjWgtTop(AdjWgtVec myVec){
    return myVec->data[myVec->sz-1];
}

/** adjWgtData()
 * precondition: 0 <= i < adjWgtSize(myVec).
 */
AdjWgt adjWgtData(AdjWgtVec myVec, int i){
    return myVec->data[i];
}

/** adjWgtSize()
 * precondition: myVec has been constructed.
 */
int adjWgtSize(AdjWgtVec myVec){
    return myVec->sz;
}

/** adjWgtCapacity()
 * precondition: myVec has been constructed.
 */
int adjWgtCapacity(AdjWgtVec myVec){
    return myVec->capacity;
}

/* Constructors
 */

/** adjWgtMakeEmptyVec()
 * preconditions: none.
 * postconditions: Let /return be the value returned by adjWgtMakeEmptyVec().
 *    Then adjWgtCapacity(/return) == 4, adjWgtSize(/return) == 0).
 */
AdjWgtVec adjWgtMakeEmptyVec(void){
    AdjWgtVec newVec;
    newVec = calloc(1,sizeof(struct AdjWgtVecNode));
    newVec->data = calloc(adjWgtInitCap, sizeof(AdjWgt));
    newVec->sz = 0;
    newVec->capacity=adjWgtInitCap;
    return newVec;
}


/* Manipulation Procedures
 */

/** adjWgtVecPush()
 * precondition: myVec has been constructed.
 * postconditions: Let /sz/ = adjWgtSize(myVec) before the call.
 *                 Let /cap/ = adjWgtCapacity(myVec) before the call.
 *    Then after the call, adjWgtSize(myVec) == /sz/+1,
 *        and adjWgtTop(myVec) == newE and adjWgtData(myVec, /sz/) == newE.
 *    Also, for all 0 <= i < /sz/: adjWgtData(myVec, i) is unchanged.
 *    Also, if (/sz/+1) > /cap/, then after the call,
 *        adjWgtCapacity(myVec) = 2 * /cap/.
 *    otherwise, adjWgtCapacity(myVec) is unchanged.
 */
void adjWgtVecPush(AdjWgtVec myVec, AdjWgt newE){
    if(myVec->sz==myVec->capacity){
        int newCap;
        newCap=2*myVec->capacity;
        AdjWgt* newData;
        newData=realloc(myVec->data,newCap*sizeof(AdjWgt));
        if(newData != myVec->data){
            myVec->data=newData;
        }
        myVec->capacity =newCap;
    }
    myVec->data[myVec->sz]=newE;
    myVec->sz=myVec->sz+1;

}

/** adjWgtVecPop()
 * precondition: myVec has been constructed and adjWgtSize(myVec) > 0.
 * postconditions: Let /sz/ = adjWgtSize(myVec) before the call.
 *                 Let /cap/ = adjWgtCapacity(myVec) before the call.
 *    Then after the call, adjWgtSize(myVec) == /sz/-1,
 *        adjWgtTop(myVec) == adjWgtData(/sz/-2).
 *    Also, for all 0 <= i < /sz/-1: adjWgtData(myVec, i) is unchanged.
 *    Also, adjWgtCapacity(myVec) is unchanged.
 */
void adjWgtVecPop(AdjWgtVec myVec){
    myVec->sz=adjWgtSize(myVec)-1;
}



