JAVASRC    = Queue.java Node.java QueueRunner.java
SOURCES    = README Makefile $(JAVASRC)
MAINCLASS  = QueueRunner
CLASSES    = Queue.class Node.class QueueRunner.class
JARFILE    = Priority.jar

all: $(JARFILE)

$(JARFILE): $(CLASSES)
	echo Main-class: $(MAINCLASS) > Manifest
	jar cvfm $(JARFILE) Manifest $(CLASSES)
	rm Manifest

$(CLASSES): $(JAVASRC)
	javac -Xlint $(JAVASRC)

clean:
	rm $(CLASSES) $(JARFILE)
