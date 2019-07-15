FLAGS = -std=c99 -Wall
SOURCES = tail.c
OBJECTS =tail.o
EXEBIN = tail

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
		gcc -o $(EXEBIN) $(OBJECTS)
$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean:
	rm -f $(EXEBIN) $(OBJECTS)
