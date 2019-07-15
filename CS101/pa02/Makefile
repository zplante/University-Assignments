FLAGS   = -std=c99 -Wall
SOURCES = graph02.c intVec.c loadGraph.c
OBJECTS = graph02.o intVec.o loadGraph.o
EXEBIN  = graph02

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
	gcc -o $(EXEBIN) $(OBJECTS)

$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean :
	rm -f $(EXEBIN) $(OBJECTS)

