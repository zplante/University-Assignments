FLAGS   = -std=c99 -Wall
SOURCES = greedy04.c adjWgtVec.c loadWgtGraph.c minPQ.c 
OBJECTS = greedy04.o adjWgtVec.o loadWgtGraph.o minPQ.o
EXEBIN  = greedy04

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
	gcc -o $(EXEBIN) $(OBJECTS)

$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean :
	rm -f $(EXEBIN) $(OBJECTS)
