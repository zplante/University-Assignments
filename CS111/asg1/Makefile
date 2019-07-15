FLAGS = -std=c99 -Wall
SOURCES = myshell.c
OBJECTS =myshell.o
EXEBIN = myshell
LEX = lex.l
LEXF = lex.yy.c
LEXOBJECT = lex.yy.o

all: $(EXEBIN)

$(EXEBIN) : $(OBJECTS)
		flex $(LEX)
		cc -o $(EXEBIN) $(OBJECTS) $(LEXF) -lfl
		
$(OBJECTS) : $(SOURCES)
	cc -c $(FLAGS) $(SOURCES) 

clean:
	rm -f $(EXEBIN) $(OBJECTS) $(LEXOBJECT) $(LEXF)