#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include "intVec.h"


//Zac Plante
//zplante

int main(int argc, char* argv[]){
    FILE* in;
    char word[256];


    /* check command line for correct number of arguments */
    if( argc != 2 ){
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* open input file for reading */
    in = fopen(argv[1], "r");
    if( in==NULL ){
        printf("Unable to read from file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    int n;
    n=atoi(fgets(word,256,in));
    int m;
    m=0;
    IntVec list[n];
    int x=0;
    while(x<n){
        list[x]=intMakeEmptyVec();
        x++;
    }
    int from;
    int to;
    int i;
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

        if(from>n||from<1){
            printf("from point is outside the range of n\n");
            exit(EXIT_FAILURE);
        }
        if(to>n||to<1){
            printf("to point is outside the range of n\n");
            exit(EXIT_FAILURE);
        }

        intVecPush(list[from-1],to);

        m++;
    }
    printf("n = %d\n",n);
    printf("m = %d\n",m);
    for(i=0;i<n;i++){
        printf("%d\t[",i+1);
        if(intSize(list[i])==0){  //use sz instead
            printf("]\n");
        }else{
            while(intSize(list[i])>1){
                printf("%d,",intTop(list[i]));
                intVecPop(list[i]);
            }
            printf("%d]\n",intTop(list[i]));
        }
    }
    fclose(in);


    return(EXIT_SUCCESS);
}



