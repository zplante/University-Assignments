#include<stdio.h>
#include<stdlib.h>
#include "adjWgtVec.h"
#include "loadWgtGraph.h"
#include "minPQ.h"
#include<string.h>

//Zac Plante
//zplante
//main method for scc03

double calculatePriority(int from,int to,double wgt,MinPQ pq, int undirected){
    if(undirected==0){
        wgt+=getPriority(pq,from-1);
    }
    return wgt;
}
void printOutput(int n,MinPQ pq, int undirected){
    char* task="Prim's MST";
    if(undirected==0){
        task="Dijkstra's SSSP";
    }
    printf("Execution of %s\n",task);
    printf("V\tStat\tFWgt\tPar\n");
    int i;
    for(i=0;i<n;i++){
        printf("%d\t%c\t%lf %d\n",i+1,getStatus(pq,i),getPriority(pq,i),getParent(pq,i));
    }

}
void updateFringe(int n,MinPQ pq,AdjWgtVec* list, int undirected){
    int v;
    for(v=0;v<n;v++) {
        if (getStatus(pq, v) == INTREE) {
            int size = adjWgtSize(list[v]);
            int i;
            for (i = 0; i < size; i++) {
                AdjWgt temp = adjWgtData(list[v], i);
                int to = temp.to;
                if (getStatus(pq, to - 1) != INTREE) {
                    double wgt = temp.wgt;
                    wgt = calculatePriority(v + 1, to, wgt, pq, undirected);

                    if (getStatus(pq, to - 1) == FRINGE) {
                        if (wgt < getPriority(pq, to - 1)) {
                            decreaseKey(pq, to - 1, wgt, v + 1);
                        }
                    } else {
                        insertPQ(pq, to - 1, wgt, v + 1);
                    }

                }
            }
        }
    }
}

int calculateIntreePoints(MinPQ pq,int n){
    int ret=0;
    int i;
    for(i=0;i<n;i++){
        if(getStatus(pq,i)==INTREE){
            ret++;
        }
    }
    return ret;
}
int calculateFringePoints(MinPQ pq,int n){
    int ret=0;
    int i;
    for(i=0;i<n;i++){
        if(getStatus(pq,i)==FRINGE){
            ret++;
        }
    }
    return ret;
}
void greedyTree(int n,AdjWgtVec * list,MinPQ pq,int undirected){
    if(n==calculateIntreePoints(pq,n)){
        return;
    }
    updateFringe(n,pq,list,undirected);
    if(calculateFringePoints(pq,n)==0){
        return;
    }else{
        delMin(pq);
        greedyTree(n,list,pq,undirected);
    }

}

int main(int argc, char* argv[]){
    FILE* in;
    int undirected=0;
    int start=0;
    char word[256];


    /* check command line for correct number of arguments */
    if(argc != 4){
        printf("Usage: %s <input file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* open input file for reading */
    in = fopen(argv[3], "r");
    if( in==NULL ){
        printf("Unable to read from file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }
        if(strcmp(argv[1],"-P")==0){
            undirected=1;
        }else if(strcmp(argv[1],"-D")==0){
                undirected=0;
        }else{
            printf("Unkown Flag %s\n", argv[1]);
            exit(EXIT_FAILURE);
        }
    start = atoi(argv[2]);


    int n;
     AdjWgtVec * list;
    list=loadWgtGraph(&n,word,in,undirected);
   int* status=calloc(n,sizeof(int));
   double* fwgt=calloc(n, sizeof(double));
   int* parent=calloc(n, sizeof(int));
    for(int i=0;i<n;i++){
        fwgt[i]=-1;
        parent[i]=-1;
        status[i]='u';
    }
    MinPQ pq;
   pq= createPQ(n,status,fwgt,parent);
    insertPQ(pq,start-1,0,-1);
    delMin(pq);
    greedyTree(n,list,pq,undirected);
    printOutput(n,pq,undirected);

    fclose(in);


    return(EXIT_SUCCESS);
}






