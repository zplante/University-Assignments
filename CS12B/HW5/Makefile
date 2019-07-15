JAVASRC    = Client.java Node.java ShakeTable.java
SOURCES    = README Makefile $(JAVASRC)
MAINCLASS  = Client
CLASSES    = Client.class Node.class ShakeTable.class
JARFILE    = Bard.jar

all: $(JARFILE)

$(JARFILE): $(CLASSES)
	echo Main-class: $(MAINCLASS) > Manifest
	jar cvfm $(JARFILE) Manifest $(CLASSES)
	rm Manifest

$(CLASSES): $(JAVASRC)
	javac -Xlint $(JAVASRC)

clean:
	rm $(CLASSES) $(JARFILE)
