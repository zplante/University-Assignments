#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <sys/time.h>
#include <stdlib.h>

#include "Superblock.h"
#include "Directory.h"

int writeblock(int fd, int index, int blocksize, void* buff){
    lseek(fd, index*blocksize, SEEK_SET);
    return write(fd, buff, blocksize);
}
int readblock(int fd, int index, int blocksize, void* buff){
    lseek(fd, index*blocksize, SEEK_SET);
    return write(fd, buff, blocksize);
}


int main(int argc, char **argv){
    if(argc!=4){
    //fail
    }
    int blocksize,blocknumber;
    char* name;
    int fd;
    name=argv[1];
    blocksize=atoi(argv[2]);
    blocknumber=atoi(argv[3]);
    void* buff = malloc(blocksize);
    fd= open(name,O_RDWR | O_CREAT);
        if(fd<0){
            //fail
        }
    
    
    //intilize super
    struct Superblock* super = buff;
    super->magicnum=0xfa91283e;
    super->totalblocks=blocknumber;
    super->fatblocks=blocknumber/(blocksize/4);
    if(blocknumber%blocksize!=0){
        super->fatblocks++;
    }
    super->blocksize= blocksize;
    super->root= super->fatblocks+1;
    writeblock(fd,0,blocksize,super);
    
    //intialize fattable
    int* array = malloc(blocksize);
    int protect = super->fatblocks;
    for(int i=0;i<super->fatblocks;i++){
        for(int j =0;j<blocksize/4;j++){
            if(j<protect){
                array[j]=-1;
            }else if(j==protect){
                array[j]=-2;
                }else{
                array[j]=0;
            }
        }
        protect-=(blocksize/4);
        writeblock(fd,1+i,blocksize,array);
    }
    struct Directory* dir = buff;
    int timenow;
    timenow = time(NULL);
    strcpy(dir->name,"root");
    dir->creationtime = timenow;
    dir->modificationtime = timenow;
    dir->accesstime = timenow;
    dir->length=64;
    dir->start = blocknumber/(blocksize/4)+1;
    dir->flags = 1;
    writeblock(fd,blocknumber/(blocksize/4)+1,blocksize,dir);

    
}