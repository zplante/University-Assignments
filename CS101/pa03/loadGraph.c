#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
#include<string.h>
#include"loadGraph.h"
//Zac Plante
//zplante
//definitions for functions in loadGraph.h

int * * makeAdjMatrix(int n, IntVec * list){
    int * * ret;
    ret=calloc(n, sizeof(int *));
    int a;
    for (a=0;a<n;a++){
        ret[a]=calloc(n,sizeof(int));
    }
    //return to this
    int i;
    int j;
    for(i=0;i<n;i++){
        for(j=0;j<intSize(list[i]);j++){
            ret[i][intData(list[i],j)-1]=1;
        }

    }
    return ret;
}
IntVec * loadGraphUndir(int *n,int *m, char * word, FILE * in){
    int x=0;
    *n=atoi(fgets(word,256,in));
    IntVec * list;
    list=calloc(*n, sizeof(IntVec));
    while(x<*n){
        list[x]=intMakeEmptyVec();
        x++;
    }
    int count=0;
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
            printf("from point is outside the range of n");
            exit(EXIT_FAILURE);
        }
        if(to>*n||to<1){
            printf("to point is outside the range of n");
            exit(EXIT_FAILURE);
        }

        intVecPush(list[from-1],to);
        intVecPush(list[to-1],from);

        count=count+2;
    }
    *m=count;
    return list;
}

IntVec * loadGraphDir(int *n,int *m,char * word, FILE * in){
    int x=0;
    *n=atoi(fgets(word,256,in));
    IntVec * list;
    list=calloc(*n, sizeof(IntVec));
    while(x<*n){
        list[x]=intMakeEmptyVec();
        x++;
    }
    int count =0;
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
            printf("from point is outside the range of n");
            exit(EXIT_FAILURE);
        }
        if(to>*n||to<1){
            printf("to point is outside the range of n");
            exit(EXIT_FAILURE);
        }

        intVecPush(list[from-1],to);


        count++;
    }
    *m=count;
    return list;
}

IntVec * transposeGraph(int n,IntVec * list){
    IntVec * ret;
    ret=calloc(n, sizeof(IntVec));
    int x=0;
    while(x<n){
        ret[x]=intMakeEmptyVec();
        x++;
    }
    int i;
    for(i=0;i<n;i++){
        while(intSize(list[i])>0){
            intVecPush(ret[intTop(list[i])-1],i+1);
            intVecPop(list[i]);
        }
    }
    return ret;
}

void printAdjVerts(int n,int m,IntVec * list){
    int i;
    printf("n = %d\n",n);
    printf("m = %d\n",m);
    for(i=0;i<n;i++){
        printf("%d\t[",i+1);
        if(intSize(list[i])==0){  //use sz instead
            printf("]\n");
        }else{
            int j;
            for(j=intSize(list[i])-1;j>0;j--){
                printf("%d,",intData(list[i],j));
            }
            printf("%d]\n",intData(list[i],j));
        }
    }
    printf("\n");
}

void printAdjMatrix(int n, int ** mtrx){
    if(n>20){
        printf("Matrix is too large to print\n");
        printf("\n");
    }else {
        int i;
        int j;
        printf("    ");
        for (i = 1; i <= n; i++) {
            if(i>9){
                printf(" %d",i);
            }else{
                printf("  %d",i);
            }
        }
        printf("\n    ");
        for(i=1;i<=n;i++){
            printf("---");
        }
        printf("\n");
        for(i=0;i<n;i++){
            if(i+1<10){
                printf(" %d :",i+1);
            }else{
                printf("%d :",i+1);
            }
            for(j=0;j<n;j++){
                printf("  %d",mtrx[i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
}


