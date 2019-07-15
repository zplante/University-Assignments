#include<stdio.h>
#include<ctype.h>
#include<stdlib.h>
#include<string.h>

void counter(char* s, int a, int n, int p, int w){
    int i;
    for(i=0;i<strlen(s)-1;i++){
        char let;
        let = s[i];
        if(isalpha((int)let)){
            a++;
        }
        if(isdigit((int)let)){
            n++;
        }
        if(ispunct((int)let)){
            p++;
        }
        if(isspace((int)let)){
            w++;
        }

    }
}

void extract_chars(char* s, char* a, char* d, char* p, char* w){
    int i;
    int ap, np, pp, wp;
    ap=np=pp=wp=0;
    for(i=0;i<strlen(s)-1;i++){
        char let;
        let = s[i];
        if(isalpha((int)let)){
            a[ap]=let;
            ap++;
        }
        if(isdigit((int)let)){
            d[np]=let;
            np++;
        }
        if(ispunct((int)let)){
            p[pp]=let;
            pp++;
        }
        if(isspace((int)let)){
            w[wp]=let;
            wp++;
        }
        a[ap+1]='\0';
        d[np+1]='\0';
        p[pp+1]='\0';
        w[wp+1]='\0';
    }



}


int main(int argc, char* argv[]){
    FILE* in;  /* file handle for input */
    FILE* out; /* file handle for output */
    char word[256]; /* char array to store words from input file */

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
        int acount, ncount, pcount, wcount;
        acount=0;
        ncount=0;
        pcount=0;
        wcount=0;
        counter(word, acount, ncount, pcount, wcount);
        char* a;
        char* n;
        char* p;
        char* w;

        a = malloc(sizeof(char)*(acount+1));
        n = malloc(sizeof(char)*(ncount+1));
        p = malloc(sizeof(char)*(pcount+1));
        w = malloc(sizeof(char)*(wcount+1));


        extract_chars(word, a, n, p, w);

        fprintf(out, "line %d contains: \n", line);
        line++;
        char* plur;
        if(strlen(a)==1){
            plur="";
        }
        else{
            plur="s";
        }
        fprintf(out, "%lu alphabetic character%s: %s\n", strlen(a),plur,a);
        if(strlen(n)==1){
            plur="";
        }
        else{
            plur="s";
        }
        fprintf(out, "%lu numeric character%s: %s\n", strlen(n),plur,n);
        if(strlen(p)==1){
            plur="";
        }
        else{
            plur="s";
        }
        fprintf(out,"%lu punctuation character%s: %s\n", strlen(p),plur,p);
        if(strlen(w)==1){
            plur="";
        }
        else{
            plur="s";
        }
        fprintf(out,"%lu whitespace character%s: %s\n", strlen(w),plur,w);
        free(a);
        a = NULL;
        free(n);
        n = NULL;
        free(p);
        p = NULL;
        free(w);
        w = NULL;
    }

    /* close input and output files */
    fclose(in);
    fclose(out);


    return(EXIT_SUCCESS);
}
