FLAGS   = -std=c99 -Wall
SOURCES = DictionaryClient.c Dictionary.c
OBJECTS = DictionaryClient.o Dictionary.o
EXEBIN  = DictionaryClient

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
	gcc -o $(EXEBIN) $(OBJECTS)

$(OBJECTS) : $(SOURCES)
	gcc -c $(FLAGS) $(SOURCES)

clean :
	rm -f $(EXEBIN) $(OBJECTS)
