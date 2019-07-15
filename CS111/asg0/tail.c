#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int error;

int	findTail(int fd){
		char buffer[1];
		int count;
		int index;
		int base[11];
		count=0;
		index=0;
		while(read(fd,buffer,1)!=0){
			index++;
			if(*buffer=='\n'){
				base[count%11]=index;
				count++;
			}
		}
		if(count<11){
			return 0;
		}else{
			return base[(count)%11];
		}
}

	
void	printTail(int fd){
		int offset;
		offset=findTail(fd);
	lseek(fd,offset,SEEK_SET);
	char buffer[1];
	while(read(fd,buffer,1)!=0){
		write(1,buffer,1);
	}
}



int main(int argc,char** argv){

	if(argc==1){
		char buffer[1];
		while(read(0,buffer,1)!=0){
		write(1,buffer,1);
		}
	}else if(argc==2){
		int fd; 
		fd = open(argv[1], O_RDONLY);
		printTail(fd);
	}else{
		for(int i=1;i<argc;i++){



		int fd;
		fd=open(argv[i],O_RDONLY);
		printTail(fd);
		}
	}
	}
