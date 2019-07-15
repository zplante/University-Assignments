//
// Zac Plante
//zplante
//functions for DFS

#ifndef UNTITLED3_DFSTRACE1_H
#define UNTITLED3_DFSTRACE1_H
static int time =1;
void trace(int place, int n,IntVec * list,char * color, int * discovery, int * finish, int * parent,IntVec stk);

void printtrace(int n,IntVec * list,char * color, int * discovery, int * finish, int * parent);


void printSTK(IntVec stk);
#endif //UNTITLED3_DFSTRACE1_H

