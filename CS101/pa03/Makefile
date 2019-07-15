FLAGS   = -std=c99 -Wall
SOURCES = scc03.c intVec.c loadGraph.c dfsTrace1.c dfsPhase2.c
OBJECTS = scc03.o intVec.o loadGraph.o dfsTrace1.o dfsPhase2.o
EXEBIN  = pa03

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
	gcc -o $(EXEBIN) $(OBJECTS)

$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean :
	rm -f $(EXEBIN) $(OBJECTS)

