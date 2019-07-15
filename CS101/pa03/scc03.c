#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
#include "loadGraph.h"
#include "dfsTrace1.h"
#include "dfsPhase2.h"
#include<string.h>

//Zac Plante
//zplante
//main method for scc03



int main(int argc, char* argv[]){
    FILE* in;
    int undirected=0;
    char word[256];


    /* check command line for correct number of arguments */
    if( argc != 2 &&argc != 3){
        printf("Usage: %s <input file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* open input file for reading */
    in = fopen(argv[1], "r");
    if( in==NULL ){
        printf("Unable to read from file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }
    if(argc==3){
        if(strcmp(argv[2],"-U")==0){
            undirected=1;
        }else{
            printf("Unkown Flag %s\n", argv[2]);
                exit(EXIT_FAILURE);
        }
    }

    int n;
    int m;
    IntVec * list;
    if(undirected){
        list=loadGraphUndir(&n,&m,word,in);
    }else {
        list = loadGraphDir(&n, &m, word, in);
    }

    char * color=calloc(n,sizeof(char));
    int * discovery=calloc(n, sizeof(int));
    int * finish=calloc(n,sizeof(int));
    int * parent=calloc(n, sizeof(int));
    IntVec stk;
	stk=intMakeEmptyVec();
    for(int i=0;i<n;i++){
        color[i]='W';
        parent[i]=-1;
    }

    printAdjVerts(n,m,list);
    trace(0,n,list,color,discovery,finish,parent,stk);
    printtrace(n,list,color,discovery,finish,parent);
    printSTK(stk);
    list=transposeGraph(n,list);
    for(int i=0;i<n;i++){
        color[i]='W';
        discovery[i]=0;
        finish[i]=0;
        parent[i]=-1;
    }
   printAdjVerts(n,m,list);
    int * root=calloc(n,sizeof(int));
    int place=intTop(stk);
    intVecPop(stk);
    trace2(place-1,list,stk,color,discovery,finish,parent,root,place);

    printtrace2(n,color,discovery,finish,parent,root);
    fclose(in);


    return(EXIT_SUCCESS);
}




