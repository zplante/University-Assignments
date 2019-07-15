//
// Zac Plante
//zplante
//functions for load and rinting graph elements

#ifndef UNTITLED3_LOADGRAPH_H
#define UNTITLED3_LOADGRAPH_H

//creates the adjency matrix of a given array of IntVecs
int ** makeAdjMatrix(int n, IntVec * list);

//loads the directed edges of a graph
IntVec * loadGraphDir(int *n,int *m,char * word, FILE * in);
//loads the undirected edges of a graph
IntVec * loadGraphUndir(int *n,int *m, char * word, FILE * in);
//trasposes graph
IntVec * transposeGraph(int n,IntVec * list);
//prints adjecency list
void printAdjVerts(int n,int m,IntVec * list);
//prints adjency matrix
void printAdjMatrix(int n, int ** mtrx);

#endif //UNTITLED3_LOADGRAPH_H

