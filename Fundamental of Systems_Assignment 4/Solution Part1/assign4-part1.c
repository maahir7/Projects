#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <fcntl.h>
#include <errno.h>
int main(int argc, char *argv[]) {
	char *fileName;
	FILE *ptr_input;
	FILE *ptr_output;

	int fd_in;
	
	struct stat st;
	unsigned long filesize;
	unsigned long * memAccesses;
	int i; 

	unsigned int pagetable[32] = {2, 4, 1, 7, 3, 5, 6 };
	unsigned int page, frame, offset;
	unsigned long phyaddr;

	if(argc != 2) {
		fprintf(stderr, "Wrong number of parameters. The correct one: ./assign3-p1 SequenceFile\n");
		exit(0); 
	}
	fileName = argv[1];
	stat(fileName, &st);	
	filesize = st.st_size;

	//allocate space
	memAccesses = (unsigned long*) malloc( (size_t) filesize );

	/*
	ptr_input = fopen(fileName, "rb"); 
	if( !ptr_input ) {
		fprintf(stderr, "unable to open the input sequence file");
		exit(-1);
		}
	*/

	//use open and read
	fd_in = open(fileName, O_RDONLY); 
	if(fd_in =open(argv[-1], O_RDONLY)) <= 0) {
		fprintf(stderr, "fd is invalid, with error %s\n");
		exit(-1);
	}
	read(fd_in, memAccesses, (int) filesize);
		
	ptr_output = fopen("output-part1", "wb"); 
	if( !ptr_output ) {
		fprintf(stderr, "unable to open the input sequence file");
		exit(-1);
	}
	
	// Traverse all elements
	for(i = 0; i < filesize/(sizeof (unsigned long)); i++) {
		// Simulate the running
	  //fread(&memAccesses[i], sizeof(unsigned long), 1, ptr_input);
	  page = (unsigned int) memAccesses[i]/128;
	  frame =  pagetable[page];
	  offset = (unsigned int)memAccesses[i]%128;
	  phyaddr = frame*128 + offset;
	  printf("logical=%#010lx: page# %u ->frame# %u : offset #%3u : physical=%#010lx\n", memAccesses[i], page, frame, offset, phyaddr);
	  fwrite(&phyaddr, sizeof(unsigned long), 1, ptr_output);	  
	  //simulateAccess(memAccesses[i]);	
	}
	fflush(ptr_output);

	close(fd_in);
	fclose(ptr_output);
}
