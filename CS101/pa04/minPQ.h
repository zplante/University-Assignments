/* minPQ.h (what is the purpose of this file? Replace this question with your comment.)
*/

#ifndef C101MinPQ
#define C101MinPQ
/* Multiple typedefs for the same type are an error in C. */

typedef struct MinPQNode * MinPQ;

#define UNSEEN ('u')
#define FRINGE ('f')
#define INTREE ('t')

/* ***************** Access functions */

/** isEmpty (pq is intialized)
*/
int isEmptyPQ(MinPQ pq);

/** getMin (pq is intialized)
*/
int getMin(MinPQ pq);

/** getStatus (pq is intialized and id<=numVertices)
*/
int getStatus(MinPQ pq, int id);

/** getParent (pq is intialized and id<=numVertices)
*/
int getParent(MinPQ pq, int id);

/** getPriority (pq is intialized and id<=numVertices)
*/
double getPriority(MinPQ pq, int id);


/* ***************** Manipulation procedures */

/** delMin (pq is intializedand not empty)
*/
void delMin(MinPQ pq);

/** insertPQ (pq is intialized)
*/
void insertPQ(MinPQ pq, int id, double priority, int par);

/** decreaseKey (pq is intialized)
*/
void decreaseKey(MinPQ pq, int id, double priority, int par);


/* ***************** Constructors */

/** createPQ (all arrays ar intialized)
*/
MinPQ createPQ(int n, int status[], double priority[], int parent[]);


#endif




