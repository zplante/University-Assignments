/* intVec.h
 * The purpose of this Header file is to provide function declerations for the intVec ADT
 */
//Zac Plante
//zplante
#ifndef C101IntVec
#define C101IntVec
/* Multiple typedefs for the same type are an error in C.
* The above ifndef and define prevent multiple copies of code below.
*/

typedef struct IntVecNode*  IntVec;

/** intInitCap: initial capacity after intMakeEmptyVec() */
static const int intInitCap = 4;

/* Access functions
 */

/** intTop()
 * Precondition: myVec has been constructed
 */
int intTop(IntVec myVec);

/** intData()
 * precondition: 0 <= i < intSize(myVec).
 */
int intData(IntVec myVec, int i);

/** intSize()
 * precondition: myVec has been constructed.
 */
int intSize(IntVec myVec);

/** intCapacity()
 * precondition: myVec has been constructed.
 */
int intCapacity(IntVec myVec);



/* Constructors
 */

/** intMakeEmptyVec()
 * preconditions: none.
 * postconditions: Let /return be the value returned by intMakeEmptyVec().
 *    Then intCapacity(/return) == 4, intSize(/return) == 0).
 */
IntVec intMakeEmptyVec(void);

/* Manipulation Procedures
 */

/** intVecPush()
 * precondition: myVec has been constructed.
 * postconditions: Let /sz/ = intSize(myVec) before the call.
 *                 Let /cap/ = intCapacity(myVec) before the call.
 *    Then after the call, intSize(myVec) == /sz/+1,
 *        and intTop(myVec) == newE and intData(myVec, /sz/) == newE.
 *    Also, for all 0 <= i < /sz/: intData(myVec, i) is unchanged.
 *    Also, if (/sz/+1) > /cap/, then after the call,
 *        intCapacity(myVec) = 2 * /cap/.
 *    otherwise, intCapacity(myVec) is unchanged.
 */
void intVecPush(IntVec myVec, int newE);

/** intVecPop()
 * precondition: myVec has been constructed and intSize(myVec) > 0.
 * postconditions: Let /sz/ = intSize(myVec) before the call.
 *                 Let /cap/ = intCapacity(myVec) before the call.
 *    Then after the call, intSize(myVec) == /sz/-1,
 *        intTop(myVec) == intData(/sz/-2).
 *    Also, for all 0 <= i < /sz/-1: intData(myVec, i) is unchanged.
 *    Also, intCapacity(myVec) is unchanged.
 */
void intVecPop(IntVec myVec);


#endif


