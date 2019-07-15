#include<stdio.h>
#include<stdlib.h>
#include "intVec.h"
#include<string.h>
#include"dfsTrace1.h"
//Zac Plante
//zplante
//definitions for functions in dfsPhase2.h

static int time2;

void trace2(int place,IntVec * list,IntVec stk,char * color, int * discovery, int * finish, int * parent,int * rootlist,int root){
    if(color[place]=='W'){
        color[place]='G';
        discovery[place]=time2;
        time2++;
        rootlist[place]=root;
        for(int i=intSize(list[place])-1;i>=0;i--){
            if(color[intData(list[place],i)-1]=='W') {
                parent[intData(list[place],i)-1]=place+1;
            }
            trace2(intData(list[place],i)-1,list,stk,color,discovery,finish,parent,rootlist,root);
        }
        color[place]='B';
        finish[place]=time2;
        time2++;
    }
    if(intSize(stk)>0){
        while(intSize(stk)>0&&color[place]!='W'){
            place=intTop(stk)-1;
            root=intTop(stk);
            intVecPop(stk);
        }
        if(intSize(stk)>=0){
            trace2(place,list,stk,color,discovery,finish,parent,rootlist,root);
        }
    }
}


void printtrace2(int n,char * color, int * discovery, int * finish, int * parent,int * root){
    printf("V\tcolor2\tdTime2\tfTime2\tparent2\tdfstRoot2\n");
    for(int i=0;i<n;i++){
        printf("%d\t%c\t%d\t%d\t%d\t%d\n",i+1,color[i],discovery[i]+1,finish[i]+1,parent[i],root[i]);
    }
    printf("\n");
}

