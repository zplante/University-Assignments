all: init_file Fatsys

init_file: 
	cc -o init_file init_file.c 

Fatsys: 
	cc -D_FILE_OFFSET_BITS=64 -I/usr/local/include/fuse  -pthread -L/usr/local/lib -lfuse -lrt Fatsys.c -o Fatsys

clean:
	rm *.o
	rm init_file
	rm Fatsys