//
// Created by Zac Plante on 6/5/17.
#include<stdio.h>
#include<stdlib.h>
#include <float.h>
#include "minPQ.h"
typedef struct MinPQNode
{
    int * status;
    int * parent;
    double * priority;
    int numVertices;
    int numPQ;
    int minVertex;
    double oo;
} MinPQNode;

typedef struct MinPQNode * MinPQ;

int isEmptyPQ(MinPQ pq) {
if(pq->numPQ==0){
    return 0;
}else{
    return 1;
}
}

int getMin(MinPQ pq){
    if(pq->minVertex==-1){
        int i;
        double minWgt;
        minWgt=pq->oo;
        for(i=0;i<pq->numVertices;i++){
            if(pq->status[i]==FRINGE){
                if(pq->priority[i]<minWgt){
                    pq->minVertex=i+1;
                    minWgt=pq->priority[i];
                }
            }
        }
    }
    return pq->minVertex;
}

int getStatus(MinPQ pq, int id){
    return pq->status[id];
}

int getParent(MinPQ pq, int id){
    return pq->parent[id];
}


double getPriority(MinPQ pq, int id){
    return pq->priority[id];
}



void delMin(MinPQ pq){
    int min=getMin(pq);
    pq->status[min-1]=INTREE;
    pq->minVertex=-1;
    pq->numPQ--;
}


void insertPQ(MinPQ pq, int id, double priority, int par){
    pq->status[id]=FRINGE;
    pq->parent[id]=par;
    pq->priority[id]=priority;
    pq->minVertex=-1;
    pq->numPQ++;
}


void decreaseKey(MinPQ pq, int id, double priority, int par){
    pq->parent[id]=par;
    pq->priority[id]=priority;
    pq->minVertex=-1;
}


MinPQ createPQ(int n, int status[], double priority[], int parent[]){
    MinPQ newPQ;
	newPQ=calloc(1,sizeof(MinPQNode));
    newPQ->status=status;
    newPQ->parent=parent;
    newPQ->priority=priority;
    newPQ->numVertices=n;
    newPQ->numPQ=0;
    newPQ->minVertex=-1;
    newPQ->oo=DBL_MAX;
    return newPQ;
}







