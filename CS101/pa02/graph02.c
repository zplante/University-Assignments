#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
#include "loadGraph.h"
#include<string.h>

//Zac Plante
//zplante
//main method for graph02



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
    printAdjVerts(n,m,list);
    printAdjMatrix(n,makeAdjMatrix(n,list));
    list=transposeGraph(n,list);
    printAdjVerts(n,m,list);
    printAdjMatrix(n,makeAdjMatrix(n,list));
    list=transposeGraph(n,list);
    printAdjVerts(n,m,list);
    printAdjMatrix(n,makeAdjMatrix(n,list));

    fclose(in);


    return(EXIT_SUCCESS);
}



