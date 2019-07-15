#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
#include<string.h>
#include"dfsTrace1.h"
//Zac Plante
//zplante
//definitions for functions in dfsTrace1.h

static int time;

void trace(int place, int n,IntVec * list,char * color, int * discovery, int * finish, int * parent,IntVec stk) {
    if (place == n) {
        return;
    }
    if (color[place]== 'W') {
        color[place] = 'G';
        discovery[place]=time;
        time++;
        for (int i = intSize(list[place])-1; i >=0; i--) {
            if(color[intData(list[place], i) - 1] =='W'){
                parent[intData(list[place], i) - 1] = place+1;
            }
            trace(intData(list[place], i) - 1, n, list, color, discovery, finish, parent, stk);
        }
        color[place] = 'B';
        finish[place]=time;
        intVecPush(stk, place + 1);
        time++;
    }
    if (parent[place] == -1) {
        while(color[place]!='W'&&place<n){
            place++;
        }
        trace(place, n, list, color, discovery, finish, parent, stk);
    }
}
void printtrace(int n,IntVec * list,char * color, int * discovery, int * finish, int * parent){
    printf("V   color\tdTime\tfTime\tparent\n");
    for(int i=0;i<n;i++){
        printf("%d\t%c\t%d\t%d\t%d\n",i+1,color[i],discovery[i],finish[i],parent[i]);
    }
    printf("\n");
}


void printSTK(IntVec stk){
    printf("FSTK:");
    for(int i=0;i<intSize(stk);i++){
        printf("  %d",intData(stk,i));
    }
    printf("\n\n");
}




