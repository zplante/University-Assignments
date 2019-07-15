FLAGS   = -std=c99 -Wall
SOURCES = graph01.c intVec.c
OBJECTS = graph01.o intVec.o
EXEBIN  = graph01

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
	gcc -o $(EXEBIN) $(OBJECTS)

$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean :
	rm -f $(EXEBIN) $(OBJECTS)
