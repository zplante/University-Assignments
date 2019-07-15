#include<stdio.h>
#include<stdlib.h>
#include "adjWgtVec.h"
#include<string.h>
#include"loadWgtGraph.h"
//Zac Plante
//zplante
//definitions for functions in loadGraph.h


AdjWgtVec * loadWgtGraph(int *n, char * word, FILE * in,int undirected){
    int x=0;
    *n=atoi(fgets(word,256,in));
    AdjWgtVec * list;
    list=calloc(*n, sizeof(AdjWgtVec));
    while(x<*n){
        list[x]=adjWgtMakeEmptyVec();
        x++;
    }
    int from;
    int to;
    double weight;
    while( fgets(word, 256, in) != NULL) {
        char *tok = strtok(word, " ");
        from = atoi(tok);
        tok = strtok(NULL, " ");
        to = atoi(tok);
        tok = strtok(NULL, " ");
        if (tok == NULL) {
            weight = 0.0;
        }else{
            sscanf(tok, "%lf", &weight);
        }

        if(from>*n||from<1){
            printf("from point is outside the range of n\n");
            exit(EXIT_FAILURE);
        }
        if(to>*n||to<1){
            printf("to point is outside the range of n\n");
            exit(EXIT_FAILURE);
        }
        AdjWgt point;
        point.to=to;
point.wgt=weight;
        adjWgtVecPush(list[from-1],point);
        if(undirected==1) {
            point.to=from;
            adjWgtVecPush(list[to - 1], point);
        }

    }
    return list;
}





