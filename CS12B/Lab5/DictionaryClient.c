#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>
#include "Dictionary.h"


int main(int argc, char* argv[]){
    FILE* in;  /* file handle for input */
    FILE* out; /* file handle for output */
    char word[256]; /* char array to store words from input file */
    Dictionary list;
    list = newDictionary();

    /* check command line for correct number of arguments */
    if( argc != 3 ){
        printf("Usage: %s <input file> <output file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    /* open input file for reading */
    in = fopen(argv[1], "r");
    if( in==NULL ){
        printf("Unable to read from file %s\n", argv[1]);
        exit(EXIT_FAILURE);
    }

    /* open output file for writing */
    out = fopen(argv[2], "w");
    if( out==NULL ){
        printf("Unable to write to file %s\n", argv[2]);
        exit(EXIT_FAILURE);
    }
    int line;
    line=1;
    /* read words from input file, print on separate lines to output file*/
    while( fgets(word, 256, in) != NULL){
        int i;
        int num;
        char number[5];
        int temp;
        temp=0;
        for(i=2;i<strlen(word);i++){
            number[temp]=word[i];
            temp++;
        }
        number[temp]='\0';
        num=atoi(number);
        char com;
        com = word[0];

        if(com == 'i'){
            insert(num,list);
            fprintf(out,"Inserted %d\n",num);
        }
        if(com == 'd'){
            delete(num,list);
            fprintf(out,"Deleted %d\n",num);
        }
        if(word[0] ==  'f'){
            char* pres;
            pres="";
            if(find(num,list)==NULL){
                pres=" not";
            }
            fprintf(out,"%d is%s present\n",num,pres);

        }
        if(word[0] == (char) 'p'){
            printDictionary(out, list);
        }
    }

    /* close input and output files */
    fclose(in);
    fclose(out);
    freeDictionary(&list);

    return(EXIT_SUCCESS);
}

