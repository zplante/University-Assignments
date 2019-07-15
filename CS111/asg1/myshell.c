#include <stdio.h> 
#include <unistd.h> 
#include <sys/types.h> 
#include <errno.h>
#include <fcntl.h>
#include <string.h>
#include <sys/wait.h>
#include <stdlib.h>

extern char **getline();

void executeCommand(char** command){
    pid_t pid =fork();
    if(pid>0){
        int status;
        waitpid(pid,&status,0);
    }else if(pid==0){
        execvp(command[0],command);
        //error
    }else{
        //error
    }
}
void execd(char* command){
    pid_t pid =fork();
    if(pid>0){
    int status;
    waitpid(pid,&status,0);
    }else if(pid==0){
        chdir(command);
    }else{
        
    }
}
int length(char** array){
    int i;
    int length;
    for(i = 0; array[i] != NULL; i++) {
    length++;
}
    return length;
}
char** sub(int min,int max,char** array){
    int size;
    size = (max-min)+1;
    if(max!=length(array)){
        size++;
    }
   char* newar[size];
   int i;
   i=0;
   while(min<=max){
       newar[i]=array[min];
       i++;
       min++;
   }
   if(newar[i-1]!=NULL){
       newar[i]=NULL;
   }
   return newar;
}
void fileOut(char** command,int index,int flag){
    int file=open(command[index+1],O_WRONLY | O_CREAT);
        if(file==-1){
            //error
        }else{
            if(flag==0){
                
            }else{
                lseek(file,0,SEEK_END);
            }
            
                int stout = dup(1);
         dup2(file,1);
                char** newcom=sub(0,index-1,command);
                executeCommand(newcom);
                dup2(stout,1);
            }
            
            close(file);
        }

void fileIn(char** command,int index){
    int file = open(command[index+1],O_RDONLY);
        if(file==-1){
            //error
        }else{
                int stin = dup(0);
                dup2(file,0);
                char** newcom=sub(0,index-1,command);
                executeCommand(newcom);
                dup2(stin,0);
          
                //error
            }
          
        close(file);
        }

void exepipe(char** command, int index){
    printf("pipe was not enabled\n");
}

int isSpecial(char* word){
    if(strcmp(word,"(")==0
        || strcmp(word,")")==0
        || strcmp(word,"<")==0
        || strcmp(word,">")==0
        || strcmp(word,"|")==0
        || strcmp(word,";")==0
        || strcmp(word,"<<")==0
        || strcmp(word,">>")==0
        || strcmp(word,"&")==0
        || strcmp(word,"cd")==0){
            return 1;
        }
        return 0;
}
int containsSpecial(char** command){
	int i;
        for(i = 0; command[i] != NULL; i++) {
        if(isSpecial(command[i])==1){
            return 1;
        }
    }
    return 0;
}


void execute(char** command){
    if(containsSpecial(command)==0){
        executeCommand(command);
    }else{
	int i;
        for(i = 0; command[i] != NULL; i++){
            if(isSpecial(command[i])==1){
            if(strcmp(command[i],">")==0){
                fileOut(command,i,0);
                break;
            }else if(strcmp(command[i],">>")==0){
                fileOut(command,i,1);
                break;
            }else if(strcmp(command[i],"<")==0){
                fileIn(command,i);
                break;
            }else if(strcmp(command[i],"|")==0){
                exepipe(command,i);
                break;
            }else if(strcmp(command[i],"cd")==0){
                execd(command[i+1]);
                break;
            }else{
                printf("Sybmol %s not supported in this shell\n",command[i]);
            }
        }
    }
}
}
int main() {

    char **args;
    while(1) {
        args = getline();
        if(args[0]==NULL){
            continue;
        }
        if(strcmp(args[0],"exit")==0){
            exit(EXIT_SUCCESS);
        }else{
            execute(args);
            }
        }
    } 

