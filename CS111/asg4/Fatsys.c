#define FUSE_USE_VERSION 30

#include <fuse.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <dirent.h>
#include <errno.h>
#include <sys/time.h>
#include <stdlib.h>

#include "Superblock.h"
#include "Directory.h"

int fd;
struct Superblock* super;
struct Directory* block;

int writeblock(int fd, int index, int blocksize, void* buff){
    lseek(fd, index*blocksize, SEEK_SET);
    return write(fd, buff, blocksize);
}
int readblock(int fd, int index, int blocksize, void* buff){
    lseek(fd, index*blocksize, SEEK_SET);
    return write(fd, buff, blocksize);
}
int getblock(int index,void* buff){
    return readblock(fd,index,super->blocksize,buff);
}
int putblock(int index,void* buff){
    return writeblock(fd,index,super->blocksize,buff);
}

char* getname(const char* path){
    int length = strlen(path);
    int last=0;
    for(int i=0;i<length;i++){
        if(path[i]=='/'){
            last = i;
        }
    }
    char ret[length-last];
    for(int i=last;i<=length;i++){
        ret[i-last]=path[i];
}
return ret;
}

static void* FAT_init(struct fuse_conn_info *conn,struct fuse_config *cfg){
	super = malloc(sizeof(struct Superblock));
	read(fd,super,sizeof(struct Superblock));
	block=calloc(super->blocksize/sizeof(struct Directory),sizeof(struct Directory));
	return NULL;
}
//first pass good

int findfreeblock(){
   int buff[super->blocksize/4];
    int value;
    for(int i = 1;i<=super->fatblocks;i++){
        readblock(fd,i,super->blocksize,buff);
        for(int j = 0;j<super->blocksize/4;j++){
            value=buff[j];
            if(value==0){
                return (i*(super->blocksize/4)+j);
            }
        }
    }
    return -1;
}
//first pass good
int checkfat(int index){
    int fatblock=(index/super->fatblocks)+1;
    int spot=index%super->fatblocks;
    int buff[super->blocksize/4];
    getblock(fatblock,buff);
    int ret = buff[spot];
    return ret;
    
}//first pass good
void changefat(int index, int value){
    int fatblock=(index/super->fatblocks)+1;
    int spot=index%super->fatblocks;
    int buff[super->blocksize/4];
    getblock(fatblock,buff);
    buff[spot]=value;
}

//first pass good
int findbypath(const char* path, struct Directory dir, int flag){
    char *pathlist[20];
    char temppath[100];
    strcpy(temppath,path);
    pathlist[0]=strtok(temppath,"/");
    int i =1;
    while(pathlist[i]-1!=NULL){
        pathlist[0]=strtok(NULL,"/");
    }
    i=0;
    int index;
    while(pathlist[i+flag]!=NULL){
        if(strcmp(pathlist[i],"root")==0){
            index=super->fatblocks+1;
            getblock(index,block);
        }else{
                int keepgoing=1;
                while(keepgoing){
                for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
                    dir = block[j];
                    if(dir.length!=-1){
                    
                    if(strcmp(pathlist[i],dir.name)==0){
                       index = dir.start;
                       keepgoing=0;
                        break;
                    }
                    }
                }
                if(keepgoing){
                    if(checkfat(index)==-2){
                        return -1;
                    }else{
                        index=checkfat(index);
                        getblock(index,block);
                    }
                 
                }
            }
            
        }
        i++;
    }
      return index;  
    }

//good
int FAT_create(const char *path, mode_t mode, struct fuse_file_info *fi){
    int index;
    index = findfreeblock();
    changefat(index,-2);
    struct Directory dir;
    int dirtoadd = findbypath(path,dir,1);
    getblock(dirtoadd,block);
     struct Directory* toadd = malloc(sizeof(struct Directory));
     int timenow;
    timenow = time(NULL);
    strcpy(toadd->name,getname(path));
    toadd->creationtime = timenow;
    toadd->modificationtime = timenow;
    toadd->accesstime = timenow;
    toadd->length=0;
    toadd->start = index;
    toadd->flags = 0;
    int keepgoing = 1;
    while(keepgoing){
    for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
     if(block[j].length==-1){
         block[j]=*toadd;
         keepgoing=0;
         break;
     }   
    }
    if(keepgoing){
        if(checkfat(dirtoadd)==-2){
            int newblock = findfreeblock();
            changefat(dirtoadd,newblock);
            changefat(newblock,-2);
            getblock(newblock,block);
            block[0]=*toadd;
            dirtoadd=newblock;
            keepgoing=0;
        }else{
            dirtoadd=checkfat(dirtoadd);
             getblock(dirtoadd,block);
        }
        
    }
    }
    putblock(dirtoadd,block);
    free(toadd);
    return 0;
}
//good
static int FAT_open(const char *path, struct fuse_file_info *fi){
    struct Directory dir;
    int index =  findbypath(path,dir,0);
    dir.accesstime=time(NULL);
    return index;
}

int FAT_write(const char *path, const char *buf, size_t size, off_t offset, 
struct fuse_file_info *fi){
    struct Directory dir;
    int index =  findbypath(path,dir,0);
    dir.modificationtime=time(NULL);
    int i=0;
    while(size>0){
    if(index==-2){
        int newblock = findfreeblock();
        changefat(index,newblock);
        changefat(newblock,-2);
        index=newblock;
        
    }
    putblock(index,buf+i*super->blocksize);
        index=checkfat(index);
        
        
        i++;
        size-=super->blocksize;
}
    return 0;
    
}
//good
int FAT_read(const char *path, char *buf, size_t size, off_t offset, 
struct fuse_file_info *fi){
    struct Directory dir;
    int index =  findbypath(path,dir,0);
    int i=0;
    while(size>0){
        if(index==-2){
            return -1;
        }
        getblock(index,buf+i*super->blocksize);
        index=checkfat(index);
        
        
        i++;
        size-=super->blocksize;
    }
    
    return 0;
    
}
//good
int FAT_unlink(const char *path){
    int index;
    int mvindex;
    struct Directory dir;
    index=findbypath(path,dir,1);
    getblock(index,block);
    mvindex=index;
    for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
        dir=block[j];
        if (dir.start ==index){
            block[j].length=-1;
            break;
        }   
    }
    putblock(index,block);
    while(mvindex!=-2){
        mvindex=checkfat(mvindex);
        changefat(index,0);
        index=mvindex;
    }
    return 0;
    
}
static int FAT_getattr(const char *path, struct stat *stbuf){
    struct Directory dir;
    int index =  findbypath(path,dir,1);
        stbuf->st_ctime= dir.creationtime;
		stbuf->st_atime= dir.accesstime;
		stbuf->st_dev = -1;
		stbuf->st_ino = -1;
		stbuf->st_nlink = 0;
		stbuf->st_mtime = dir.modificationtime;
		stbuf->st_size = super->totalblocks * super->blocksize;
		stbuf->st_blksize = super->blocksize;
		stbuf->st_blocks = super->totalblocks;
		stbuf->st_uid = -1;
		stbuf->st_gid = -1;
		stbuf->st_mode = 0;
    return 0;
}
static int FAT_readdir(const char *path, void *buf, fuse_fill_dir_t filler, off_t offset, struct fuse_file_info *fi){
    struct Directory dir;
    int index =  findbypath(path,dir,0);
    int i=0;
    while(checkfat(index)!=-2){
       
        getblock(index,buf+i*super->blocksize);
        index=checkfat(index);
        
        
        i++;
        
    }
    
    return 0;
}
//good
static int FAT_mkdir(const char *path, mode_t mode){
    struct Directory dir;
    struct Directory forlater;
     struct Directory* toadd = malloc(sizeof(struct Directory));
    int timenow;
    timenow = time(NULL);
    int newblock=findfreeblock();
    changefat(newblock,-2);
    strcpy(toadd->name,getname(path));
    toadd->creationtime = timenow;
    toadd->modificationtime = timenow;
    toadd->accesstime = timenow;
    toadd->length=0;
    toadd->start = newblock;
    toadd->flags = 1;
    int index =  findbypath(path,dir,1);
    forlater=block[0];
    int keepgoing =1;
    while(keepgoing){
    for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
        if(block[j].length==-1){
            //here
    block[j]=*toadd;
    putblock(index,block);
    keepgoing =0;
    break;
        }   
    }
    if(keepgoing){
        if(checkfat(index)==-2){
            int newindex = findfreeblock();
            if(newindex==-1){
                keepgoing=0;
                break;
            }
            changefat(index,newindex);
            changefat(newindex,-2);
            getblock(newindex,block);
            block[0]=*toadd;
            putblock(index,block);
    keepgoing =0;
        }else{
            index=checkfat(index);
             getblock(index,block);
        }
    }
    getblock(newblock,block);
    strcpy(toadd->name,".");
    block[0]=*toadd;
    strcpy(forlater.name,"..");
    block[1]=forlater;
    putblock(newblock,block);
    free(toadd);
    return 0;
}
return -1;
}
static int FAT_rmdir(const char *path){
    struct Directory dir;
    int index =  findbypath(path,dir,0);
    for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
        dir=block[j];
        if(dir.start==index){
            block[j].length=-1;
            break;
        }
    }
    getblock(index,block);
    for(int j=0;j<super->blocksize/sizeof(struct Directory);j++){
    dir=block[j];
    char temppath[100];
    strcpy(temppath,path);
    if(dir.flags==1){
            FAT_rmdir(strcat(temppath,strcat("/",dir.name)));
        }else{
            FAT_unlink(strcat(temppath,strcat("/",dir.name)));
        }
    }
    return 0;
    
}

static struct fuse_operations FAT_oper = {
	.open		= FAT_open, //done
	.read		= FAT_read, //done
	.write		= FAT_write, //done
	.init       = FAT_init, //done
	.readdir	= FAT_readdir, //done
	.getattr    = FAT_getattr, //done
	.mkdir      = FAT_mkdir, //done
	.rmdir      = FAT_rmdir, //done
	.unlink		= FAT_unlink, //done
	.create		= FAT_create //done
};

int main(int argc, char *argv[]){
	fd = open("disc.img", O_RDWR);
	return fuse_main(argc, argv, &FAT_oper, NULL);
}